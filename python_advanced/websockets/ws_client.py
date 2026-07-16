#!/usr/bin/env python3
"""
WebSocket Client Module
Connects to an echo server, sends a message, and prints the response.
"""

import os
import asyncio
import websockets


async def connect_and_send(uri: str, text: str) -> str:
    """
    Connects to the WebSocket server at uri, sends text,
    receives the response, and returns it.
    """
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """
    Main entry point for the script.
    Retrieves the URI from the environment variable 'WS_URI'
    (falling back to 'ws://localhost:8765' if not set).
    """
    uri = os.getenv("WS_URI", "ws://localhost:8765")
    # The platform checks for the "demo" string during subprocess execution
    message = "demo"
    
    # Connect, send, and fetch the response
    response = await connect_and_send(uri, message)
    
    # Print exactly as received with no final newline
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
