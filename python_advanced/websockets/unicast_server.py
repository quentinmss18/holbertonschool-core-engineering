#!/usr/bin/env python3
"""
Unicast WebSocket server implementation tracking active client connections.
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

# Global set to keep track of active client connections
connected_clients = set()


async def connection_handler(websocket):
    """
    Handles individual client connections. Tracks connections in a global set
    and responds in a unicast manner, sending responses only to the sender.
    """
    # Register the connection
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Send response only to the connection that initiated it
            await websocket.send(f"U:{message}")
    except ConnectionClosed:
        # Gracefully handle client disconnection
        pass
    finally:
        # Clean up connection reference on disconnect
        connected_clients.discard(websocket)


async def main():
    """
    Starts the asynchronous WebSocket server on 127.0.0.1:8765.
    """
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        # Keeps the server running indefinitely
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
