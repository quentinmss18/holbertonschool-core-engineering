#!/usr/bin/env python3
"""
WebSocket server implementation with payload verification and message validation.
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """
    Handles incoming connections and validates individual messages.
    Rejects empty or whitespace-only messages with 'ERR:EMPTY' while
    preserving original string spacing for valid payloads prefixed with 'OK:'.
    """
    try:
        async for message in websocket:
            message_str = str(message)
            
            # Check if message is empty or contains only whitespace
            if len(message_str.strip()) == 0:
                await websocket.send("ERR:EMPTY")
            else:
                # Respond with original string preserved intact
                await websocket.send(f"OK:{message_str}")
    except ConnectionClosed:
        # Catch and handle client disconnects gracefully without crashing
        pass


async def main():
    """
    Starts the asynchronous WebSocket server on localhost:8765.
    """
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        # Keep server running indefinitely
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
