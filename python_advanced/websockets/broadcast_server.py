#!/usr/bin/env python3
"""
WebSocket Server Module with broadcast capability.
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

# Set to keep track of active client connections
CLIENTS = set()


async def connection_handler(websocket):
    """
    Handles a client connection. Registers the client, listens
    for messages, and broadcasts them with a prefix of 'B:'.
    Unregisters the client upon disconnection.
    """
    # Register the active client
    CLIENTS.add(websocket)
    try:
        async for message in websocket:
            # Prepare the broadcast message
            broadcast_msg = f"B:{message}"
            # Send to all currently connected clients
            if CLIENTS:
                await asyncio.gather(
                    *[client.send(broadcast_msg) for client in CLIENTS]
                )
    except ConnectionClosed:
        pass
    finally:
        # Unregister client upon disconnection
        CLIENTS.remove(websocket)


async def main():
    """
    Main entry point to start the broadcast server.
    """
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
