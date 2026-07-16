#!/usr/bin/env python3
"""
ASGI web server application using Starlette and Uvicorn.
Handles both HTTP web pages and an asynchronous WebSocket echo endpoint.
"""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """
    HTTP route handler that serves a simple HTML web page.
    """
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    """
    WebSocket route handler that accepts a connection and continuously 
    echoes back any incoming text messages to the sender.
    """
    await websocket.accept()
    try:
        while True:
            # Continuously wait for text messages from the client
            message = await websocket.receive_text()
            # Echo the exact message back to the sender
            await websocket.send_text(message)
    except WebSocketDisconnect:
        # Cleanly handle client disconnection states
        pass


# Starlette application instantiation with defined routing configurations
app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
