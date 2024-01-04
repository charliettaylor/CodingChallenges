import json
import asyncio
from dataclasses import dataclass


@dataclass
class User:
    username: str
    writer: asyncio.StreamWriter


HOST = "0.0.0.0"
PORT = 8888

users: list[User] = []


async def handle(r: asyncio.StreamReader, w: asyncio.StreamWriter) -> None:
    async def send(data: str) -> None:
        print(data)
        w.write(data.encode("utf8"))
        w.write(b"\n")
        await w.drain()

    async def broadcast(user: User, data: str) -> None:
        print(data)
        for user in [x for x in users if x != user]:
            user.writer.write(data.encode("utf8"))
            user.writer.write(b"\n")
            await user.writer.drain()

    await send("Welcome to budgetchat! What shall I call you?")
    username = (await r.readline()).decode().strip()
    user = User(username, w)

    if len(username) == 0 or not username.isalnum():
        await w.drain()
        w.close()

    listedUsers = ",".join([x.username for x in users])
    await send("* The room contains: " + listedUsers)
    users.append(user)
    await broadcast(user, f"* {username} has entered the room")

    while True:
        try:
            message = await r.readline()

            if not message:
                break

            await broadcast(user, f"[{username}] {message.decode().strip()}")
        except Exception as e:
            print(e)
            break

    users.remove(user)
    await broadcast(user, f"* {username} has left the room")
    w.close()


async def main() -> None:
    server = await asyncio.start_server(handle, HOST, PORT)
    print(f"server running on port {PORT}.")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
