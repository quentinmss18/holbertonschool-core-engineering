#!/usr/bin/env python3
"""
Broadcast WebSocket server implementation distributing messages to all active clients.
"""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

# Global set to keep track of active client connections
connected_clients = set()


async def broadcast(message):
    """
    Sends the broadcast message to all currently connected clients.
    """
    if connected_clients:
        # Create send tasks for all connected clients to run them concurrently
        send_tasks = [
            asyncio.create_task(client.send(message))
            for client in connected_clients
        ]
        # Wait for all send tasks to finish, ignoring individual errors
        # if a client disconnects mid-broadcast
        await asyncio.gather(*send_tasks, return_exceptions=True)


async def connection_handler(websocket):
    """
    Handles individual client connections. Tracks connections globally,
    receives messages, and broadcasts them to everyone prefixed with 'B:'.
    """
    # Register the connection
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the received message to all connected clients
            await broadcast(f"B:{message}")
    except ConnectionClosed:
        # Gracefully handle individual client disconnections
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
