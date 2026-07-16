#!/usr/bin/env python3
"""
ASGI Server Module using Starlette.
Handles HTTP requests on / and WebSocket connections on /ws.
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """
    Serves a simple HTML page at the root URL.
    """
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    """
    Handles incoming WebSocket connections at /ws.
    Accepts connection and echoes received messages back to the sender.
    """
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


# Starlette application instance with defined routes
app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
