import asyncio
import websockets
from aioconsole import ainput, aprint


user_websocket = {}


async def main_1(websocket, path):
    try:
        await ask_for_nickname(websocket)
        while True:
            await list_the_connected_users(websocket)
            message = await websocket.recv()
            if message == f'{user_websocket[websocket]}: GROUP':
                await websocket.send("You are connected to group chat, feel free to chat!")
                while True:
                    message = await websocket.recv()
                    if message == f'{user_websocket[websocket]}: CHANGE ROOM':
                        break
                    await broadcast_for_group_chat(message)
            else:
                for socket, nick in user_websocket.items():
                    message1 = message.split(':')
                    print(message1[1].strip())
                    if nick == message1[1].strip():
                        await websocket.send(f"You are connected to {nick}")
                        while True:
                            message = await websocket.recv()
                            if message == f'{user_websocket[websocket]}: CHANGE ROOM':
                                break
                            await sender_for_two_clients(socket, message)
                        if message == f'{user_websocket[websocket]}: CHANGE ROOM':
                            break
    except websockets.exceptions.ConnectionClosedOK:
        pass


async def ask_for_nickname(websocket):
    await websocket.send('Please write your nickname')
    await aprint(">>> send")
    name = await websocket.recv()
    user_websocket.update({websocket: name})
    await aprint(f"<<< {name} {websocket}")
    await websocket.send('thanks')


async def list_the_connected_users(websocket):
    await websocket.send('Here are nicknames of connected users,\
                 please select with whom you want to send message\n')
    for values in user_websocket.values():
        await websocket.send(f" {values}\n")
    await websocket.send('or enter group chat, typing \'GROUP\'')


async def broadcast_for_group_chat(message):
    for websocket in user_websocket.keys():
        await websocket.send(message)


async def sender_for_two_clients(websocket, message):
    await websocket.send(message + ' [Private message]')


async def main():
    async with websockets.serve(main_1, "localhost", 8777):
        await asyncio.Future()


async def generator_of_prime_public_key():



asyncio.run(main())
