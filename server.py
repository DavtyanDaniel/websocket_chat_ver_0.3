import asyncio
import websockets


nicknames = []
clients = []


async def main_1(websocket, path):
    await ask_for_name(websocket)



async def ask_for_name(websocket):
    name = await websocket.recv()
    nicknames.append(name)
    clients.append(websocket)
    print(f"<<< {name} {websocket}")

async def list_the_connected_users(websocket):
    websocket.send('Here are nicknames of connected users,\
                 please select with whom you want to send message\n')
    for nick in nicknames:
        websocket.send(f"{nicknames.index(nick)} {nick}\n")
    websocket.send('or enter group chat, typing \'GROUP\'')
    number_of_the_user = await websocket.recv()
    return number_of_the_user


async def broadcast_for_group_chat(message):
    for client in clients:
        client.send(message)


async def main():
    async with websockets.serve(main_1, "localhost", 8766):
        await asyncio.Future()


asyncio.run(main())
