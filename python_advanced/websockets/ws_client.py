#!/usr/bin/env python3
"""
A minimal asynchronous WebSocket client that connects to an echo server,
sends a single message, receives the response, and returns it.
"""

import asyncio
import websockets


async def connect_and_send(uri, text):
    """
    Connects to the given WebSocket URI, sends a single text message,
    waits for a single response from the server, and returns it.
    The connection is cleanly closed upon exiting the context manager.
    """
    async with websockets.connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return str(response)


async def main():
    """
    Main function to execute the client logic standalone.
    Connects to ws://127.0.0.1:8765, sends 'Hello WebSocket',
    and prints the output with no final newline.
    """
    uri = "ws://127.0.0.1:8765"
    message = "Hello WebSocket"
    
    response = await connect_and_send(uri, message)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
