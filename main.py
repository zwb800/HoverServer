from websockets.server import serve, WebSocketServerProtocol
import asyncio
from hovercommand import HoverCommand


async def hello(websocket: WebSocketServerProtocol):
    while True:
        message = await websocket.recv()
        if isinstance(message, bytes):
            steer = int.from_bytes([message[0]], 'little', signed=True)
            speed = int.from_bytes([message[1]], 'little', signed=True)
            hoverCommand.send(steer,speed)


async def main():
    async with serve(hello, '0.0.0.0', 8765):
        await asyncio.Future()

hoverCommand = HoverCommand()
asyncio.run(main())
