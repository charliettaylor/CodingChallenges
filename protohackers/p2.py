from ast import Tuple
from functools import lru_cache
import json
import asyncio
from operator import truediv
from statistics import mean

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
    def send(data: int):
        print('sent', data.to_bytes(length=4, byteorder='big', signed=True))
        w.write(data.to_bytes(length=4, byteorder='big', signed=True))

    prices: list[tuple[int, int]] = []
    print('here')
    while not r.at_eof():
        try:
            bs = await r.readexactly(9)
            if len(bs) < 9:
                continue
            op = bs[0]
            left = int.from_bytes(bs[1:5], 'big', signed=True)
            right = int.from_bytes(bs[5:], 'big', signed=True)
            print(op, left, right)

            if chr(op) == "I":
                prices.append((left, right))
            elif chr(op) == "Q":
                inrange = list(filter(lambda x: x[0] >= left and x[0] <= right, prices))
                tot = sum([x[1] for x in inrange])
                print('total', tot)

                if tot != 0:
                    send(tot // len(inrange))
                else:
                    send(0)
            else:
                raise ValueError()
        except:
            print('thing no work')

    await w.drain()
    w.close()


async def main() -> None:
    server = await asyncio.start_server(handle, HOST, PORT)
    print(f"server running on port {PORT}.")
    async with server:
        await server.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
