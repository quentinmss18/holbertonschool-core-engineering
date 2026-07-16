#!/usr/bin/python3
"""
A minimal asynchronous WebSocket server that echoes back any received message.
"""

import asyncio
import websockets


async def connection_handler(websocket):
    """
    Handles an individual incoming WebSocket connection.
    Continuously loops to process text messages as they arrive
    and immediately echoes them back exactly as received.
    """
    async for message in websocket:
        await websocket.send(message)


async def main():
    """
    Initializes and runs the standalone WebSocket server on localhost:8765.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        # Keeps the server running indefinitely
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
