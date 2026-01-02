"""
FastMCP server that exposes Groq-powered weather tools.

Usage:
    1. Create a .env file with GROQ_API_KEY (and optionally OPENWEATHER_API_KEY).
    2. Run the server:
           python tool-calling/fastmcp_groq_weather_server.py
    3. In another shell, call the MCP tool via the reference CLI:
           npx @modelcontextprotocol/cli call \
               --server.command python \
               --server.args "tool-calling/fastmcp_groq_weather_server.py" \
               --tool groq-weather-server/get_weather_with_groq \
               --params '{"query":"What is the weather like in Bengaluru?"}'

The CLI command above uses the official MCP reference client to connect over
STDIO. You can also point FastMCP's Python client at this script for in-memory
testing (see README for details).
"""

from __future__ import annotations

import json
import os
from typing import Dict, List

import requests
from dotenv import load_dotenv
from groq import Groq
from mcp.server.fastmcp import FastMCP

load_dotenv()


def require_env(var_name: str) -> str:
    """Return an environment variable or raise a helpful error if missing."""

    value = os.getenv(var_name)
    if not value:
        raise EnvironmentError(
            f"Missing required environment variable: {var_name}. "
            "Create a .env file or export it before running the server."
        )
    return value


mcp = FastMCP("groq-weather-server")
client = Groq(api_key=require_env("GROQ_API_KEY"))


def get_current_weather(location: str) -> str:
    """
    Fetch live weather data from OpenWeatherMap if OPENWEATHER_API_KEY is set.

    Falls back to a deterministic demo payload so the server still works even
    without the external dependency.
    """

    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key:
        return json.dumps(
            {
                "location": location,
                "temperature_c": 24.0,
                "feels_like_c": 25.2,
                "description": "partly cloudy (demo)",
                "note": "Set OPENWEATHER_API_KEY for real data.",
            }
        )

    params = {"q": location, "units": "metric", "appid": api_key}
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


def tool_schema() -> List[Dict]:
    """Return the Groq tool definition (used in both LLM calls)."""

    return [
        {
            "type": "function",
            "function": {
                "name": "get_current_weather",
                "description": "Get the current weather in a given location",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "location": {
                            "type": "string",
                            "description": "City and optional country (e.g. Bengaluru, IN)",
                        }
                    },
                    "required": ["location"],
                },
            },
        }
    ]


@mcp.tool()
def get_weather_with_groq(query: str) -> str:
    """
    Let Groq's LLM decide whether to call get_current_weather, then return the reply.
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[{"role": "user", "content": query}],
        temperature=0,
        max_tokens=300,
        tools=tool_schema(),
        tool_choice="auto",
    )
    groq_response = response.choices[0].message

    tool_calls = groq_response.tool_calls or []
    if not tool_calls:
        return groq_response.content or "Model did not return any content."

    args = json.loads(tool_calls[0].function.arguments)
    weather_data = get_current_weather(**args)

    second_response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "user", "content": query},
            {
                "role": "assistant",
                "content": groq_response.content,
                "tool_calls": [
                    {
                        "id": tool_calls[0].id,
                        "type": tool_calls[0].type,
                        "function": {
                            "name": tool_calls[0].function.name,
                            "arguments": tool_calls[0].function.arguments,
                        },
                    }
                ],
            },
            {
                "role": "tool",
                "tool_call_id": tool_calls[0].id,
                "content": weather_data,
            },
        ],
        temperature=0,
        max_tokens=300,
    )

    return second_response.choices[0].message.content


@mcp.tool()
def get_weather_direct(location: str) -> str:
    """
    Bypass the LLM entirely and return the structured weather payload directly.
    """

    return get_current_weather(location)


if __name__ == "__main__":
    mcp.run()

