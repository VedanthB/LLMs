"""
Demo showcasing OpenAI function calling to fetch live stock prices via yfinance.

Usage:
    python tool-calling/openai_stock_function_call.py --symbol "TECHM.NS"

The script issues a chat completion request with a stock-price tool definition,
lets the model decide whether to call the tool, runs the tool locally with
yfinance, and then sends the structured result back to the model for a natural
language answer.
"""

import argparse
import json
import os
from typing import Dict, List

import yfinance as yf
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def require_env(var_name: str) -> str:
    """Return an environment variable or raise a helpful error if missing."""

    value = os.getenv(var_name)
    if not value:
        raise EnvironmentError(
            f"Missing required environment variable: {var_name}. "
            "Add it to your .env or export it before running the script."
        )
    return value


client = OpenAI(api_key=require_env("OPENAI_API_KEY"))


def get_current_stock_price(stock_symbol: str) -> str:
    """
    Fetch the most recent closing price for the provided stock ticker.

    yfinance pulls data from Yahoo Finance. We request the most recent trading
    day's close, then return a JSON string to satisfy the tool interface.
    """

    if not stock_symbol:
        return json.dumps({"error": "Missing stock_symbol argument."})

    try:
        ticker = yf.Ticker(stock_symbol)
        history = ticker.history(period="1d")
    except Exception as exc:  # yfinance raises a variety of exceptions
        return json.dumps({"error": f"Unable to fetch data for {stock_symbol}: {exc}"})

    if history.empty:
        return json.dumps({"error": f"No pricing data returned for {stock_symbol}."})

    latest_row = history.iloc[-1]
    price_data = {
        "stock_symbol": stock_symbol,
        "close_price": round(float(latest_row["Close"]), 4),
        "currency": ticker.fast_info.get("currency", "UNKNOWN"),
        "timestamp": latest_row.name.isoformat(),
    }
    return json.dumps(price_data)


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_stock_price",
            "description": "Get the most recent close price for a stock ticker using Yahoo Finance.",
            "parameters": {
                "type": "object",
                "properties": {
                    "stock_symbol": {
                        "type": "string",
                        "description": "Ticker symbol such as TECHM.NS, AAPL, or RELIANCE.NS.",
                    }
                },
                "required": ["stock_symbol"],
            },
        },
    }
]


def call_model_with_tools(question: str) -> None:
    """
    Ask the model the user's question, fulfill any tool calls, and print the reply.
    """

    initial_messages: List[Dict[str, str]] = [
        {
            "role": "system",
            "content": (
                "You are an enthusiastic financial assistant. "
                "Use the provided tools to ensure prices are accurate."
            ),
        },
        {"role": "user", "content": question},
    ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=initial_messages,
        temperature=0,
        max_tokens=300,
        tools=tools,
        tool_choice="auto",
    )

    assistant_message = response.choices[0].message
    print("\nInitial assistant response:")
    print(assistant_message)

    tool_calls = assistant_message.tool_calls or []
    tool_messages = []
    for call in tool_calls:
        if call.function.name != "get_current_stock_price":
            print(f"Skipping unsupported tool call: {call.function.name}")
            continue

        args = json.loads(call.function.arguments)
        print("\nTool call arguments:", args)
        tool_output = get_current_stock_price(**args)
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
        print("\nModel response without tool call:")
        print(assistant_message.content)
        return

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
        model="gpt-3.5-turbo",
        messages=follow_up_messages,
        temperature=0.2,
        max_tokens=400,
    )

    print("\nFinal assistant reply:")
    print(final_response.choices[0].message.content)


def parse_cli_args() -> argparse.Namespace:
    """Provide a --symbol flag so users can pick any ticker."""

    parser = argparse.ArgumentParser(
        description="Demonstrate OpenAI function calling with a stock-price tool."
    )
    parser.add_argument(
        "--symbol",
        default="TECHM.NS",
        help="Ticker symbol to query (default: TECHM.NS).",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point for CLI usage."""

    args = parse_cli_args()
    question = f"What is the price of {args.symbol}?"

    print(f"Asking the model: {question}")
    call_model_with_tools(question)


if __name__ == "__main__":
    main()

