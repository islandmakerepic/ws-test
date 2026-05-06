import asyncio
import websockets
import time
from http import HTTPStatus

async def handler(websocket):
    async for message in websocket:
        await websocket.send(f"{message}|{time.time()}")

async def health_check(path, request_headers):
    if request_headers.get("Upgrade", "").lower() != "websocket":
        return HTTPStatus.OK, [], b"OK"

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765, process_request=health_check):
        await asyncio.Future()

asyncio.run(main())
