from functools import lru_cache
import json
import asyncio

HOST = "0.0.0.0"
PORT = 8888

@lru_cache
def is_prime(n) -> bool:
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


async def handle(r: asyncio.StreamReader, w: asyncio.StreamWriter):
    def send(data: dict):
        w.write(json.dumps(data).encode('utf8'))
        w.write(b"\n")

    while not r.at_eof():
        try:
            text = await r.readuntil(b"\n")
            j = json.loads(text.decode('utf8'))
            method = j["method"]
            number = j["number"]

            if method != "isPrime":
                raise ValueError()
            
            if type(number) == int:
                send({"method": method, "prime": is_prime(number)})
            elif type(number) == float:
                send({"method": method, "prime": False})
            else:
                raise TypeError()

        except json.JSONDecodeError:
            send({"error": "error"})
            break
        except (ValueError, TypeError, KeyError):
            send({"error": "error"})
            break
        except asyncio.LimitOverrunError:
            send({"error": "error"})
            break

    await w.drain()
    w.close()


async def main() -> None:
    server = await asyncio.start_server(handle, HOST, PORT)
    print(f"server running on port {PORT}.")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
