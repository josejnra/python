import asyncio

import httpx

URL = "http://localhost:8000"


async def endpoint_1():
    async with httpx.AsyncClient(http2=True) as client:
        for _ in range(10):
            r = await client.get(f"{URL}/page-1")
            print(r.text)


async def endpoint_2():
    async with httpx.AsyncClient(http2=True) as client:
        for _ in range(10):
            r = await client.get(f"{URL}/page-2")
            print(r.text)


async def main():
    await asyncio.gather(endpoint_1(), endpoint_2())


if __name__ == "__main__":
    asyncio.run(main())
