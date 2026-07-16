#!/usr/bin/env python3
"""
WebSocket Server Module with message validation.
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """
    Handles a single client connection.
    Continuously receives messages, validates them,
    and returns either OK: or ERR: responses.
    """
    try:
        async for message in websocket:
            # Check if the message is empty after stripping whitespace
            if len(message.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                # Keep original string exactly as received (with whitespaces)
                await websocket.send(f"OK:{message}")
    except ConnectionClosed:
        pass


async def main():
    """
    Main entry point to start the server.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
