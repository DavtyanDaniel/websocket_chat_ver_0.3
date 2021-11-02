import websockets
import asyncio


async def send_name():
    uri = "ws://localhost:8766"
    async with websockets.connect(uri) as websocket:
        name = input('What is your name?')
        await websocket.send(name)
        print(f">>>> {name}")
        surname = input('Enter your surname')
        await websocket.send(surname)

        greeting = await websocket.recv()
        print(f'<<< {greeting}')

asyncio.run(send_name())
