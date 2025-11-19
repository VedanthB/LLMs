"""
End-to-end example showing how to use Groq's OpenAI-compatible API with
function calling to fetch live weather data from OpenWeatherMap.

Run this script after setting the GROQ_API_KEY and OPENWEATHER_API_KEY
environment variables (see instructions in the README or in the assistant
response). The script asks the LLM for the weather in a given location, lets
the model decide whether to call the weather tool, executes the tool, and
then sends the tool output back to the LLM for a final natural-language
answer.

Example command (run from repo root or after activating the conda env):
    python tool-calling/groq_weather_function_call.py --location "Bengaluru, IN"

Sample output (truncated):
    Asking the model: What is the weather like in Bengaluru, IN?
    ...
    Tool output (JSON): {"location": "Bengaluru, IN", "temperature_c": 26.87, ...}
    Final assistant reply:
    🌤️ Bengaluru, IN – Current Weather
    - Temperature: 26.9 °C (≈ 80 °F)
    - Feels like: 27.7 °C
    - Humidity: 57 %
    - Pressure: 1011 hPa
    - Wind: 7.2 m/s (≈ 26 km/h)
    - Conditions: Scattered clouds
    It’s a pleasant, mild day—perfect for a stroll in the city or a quick coffee break.
"""

import argparse
import json
import os
from typing import Dict, List

import requests
from dotenv import load_dotenv
from groq import Groq

# Automatically pull variables from a local .env file if present.
load_dotenv()


def require_env(var_name: str) -> str:
    """Return an environment variable or raise a clear error if it is missing."""

    value = os.getenv(var_name)
    if not value:
        raise EnvironmentError(
            f"Missing required environment variable: {var_name}. "
            "Create a .env file or export it in your shell."
        )
    return value


# Instantiate the Groq client up front so we can reuse the HTTP session.
client = Groq(api_key=require_env("GROQ_API_KEY"))


def get_current_weather(location: str) -> str:
    """
    Fetch the current weather for the supplied location using OpenWeatherMap.

    This function is registered as a "tool" so the LLM can choose to call it
    when it needs structured weather data. The result is returned as a JSON
    string to match the tool-calling contract.
    """

    api_key = require_env("OPENWEATHER_API_KEY")
    params = {
        "q": location,
        "units": "metric",  # Use Celsius so the response is globally friendly.
        "appid": api_key,
    }

    try:
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=params,
            timeout=10,
        )
        response.raise_for_status()
    except requests.RequestException as exc:
        return json.dumps({"error": f"OpenWeatherMap request failed: {exc}"})

    payload = response.json()
    weather = {
        "location": location,
        "temperature_c": payload["main"]["temp"],
        "feels_like_c": payload["main"]["feels_like"],
        "humidity_pct": payload["main"]["humidity"],
        "pressure_hpa": payload["main"]["pressure"],
        "wind_speed_mps": payload["wind"]["speed"],
        "description": payload["weather"][0]["description"],
        "icon": payload["weather"][0]["icon"],
    }
    return json.dumps(weather)


# Describe the tool so the LLM knows when/how to call it.
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and optional country (e.g. Bengaluru, IN).",
                    }
                },
                "required": ["location"],
            },
        },
    }
]


def call_model_with_tools(question: str) -> None:
    """
    Orchestrate the two-step tool-calling flow:
    1. Ask the LLM the user's question and let it decide whether to call a tool.
    2. If it calls the weather tool, execute it locally and send the result back
       to the LLM for a natural-language answer.
    """

    initial_messages: List[Dict[str, str]] = [
        {
            "role": "system",
            "content": "You are a friendly weather assistant that uses tools when needed.",
        },
        {"role": "user", "content": question},
    ]

    # Step 1: Ask the model the question with the tool definition attached.
    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=initial_messages,
        temperature=0,
        max_tokens=300,
        tools=tools,
        tool_choice="auto",
    )

    assistant_message = response.choices[0].message
    print("\nInitial assistant response (should contain a tool call):")
    print(assistant_message)

    tool_calls = assistant_message.tool_calls or []
    if not tool_calls:
        print("Model did not request a tool. Direct answer:")
        print(assistant_message.content)
        return

    # Execute each requested tool call locally.
    tool_messages = []
    for call in tool_calls:
        if call.function.name != "get_current_weather":
            print(f"Skipping unknown tool: {call.function.name}")
            continue

        args = json.loads(call.function.arguments)
        print("\nTool call arguments from the model:", args)

        tool_output = get_current_weather(**args)
        print("Tool output (JSON):", tool_output)

        tool_messages.append(
            {
                "role": "tool",
                "tool_call_id": call.id,
                "name": call.function.name,
                "content": tool_output,
            }
        )

    if not tool_messages:
        print("No tool output to send back to the model; stopping here.")
        return

    # Step 2: Send the tool outputs back to the LLM for a final response.
    follow_up_messages: List[Dict[str, object]] = initial_messages + [
        {
            "role": "assistant",
            "content": assistant_message.content,
            "tool_calls": [
                {
                    "id": call.id,
                    "type": call.type,
                    "function": {
                        "name": call.function.name,
                        "arguments": call.function.arguments,
                    },
                }
                for call in tool_calls
            ],
        },
        *tool_messages,
    ]

    final_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=follow_up_messages,
        temperature=0.2,
        max_tokens=400,
    )

    print("\nFinal assistant reply:")
    print(final_response.choices[0].message.content)


def parse_cli_args() -> argparse.Namespace:
    """Allow overriding the default city from the command line."""

    parser = argparse.ArgumentParser(
        description="Demo Groq function calling with an OpenWeatherMap tool."
    )
    parser.add_argument(
        "--location",
        default="Bengaluru, IN",
        help="City to ask about (defaults to 'Bengaluru, IN').",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point when executing the module as a script."""

    args = parse_cli_args()
    question = f"What is the weather like in {args.location}?"

    print(f"Asking the model: {question}")
    call_model_with_tools(question)


if __name__ == "__main__":
    main()

