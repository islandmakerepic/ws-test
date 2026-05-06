import asyncio
import websockets
import time

async def handler(websocket):
    async for message in websocket:
        await websocket.send(f"{message}|{time.time()}")

async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        await asyncio.Future()

asyncio.run(main())
