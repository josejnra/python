import asyncio

import aiohttp
import httpx

URL = "http://localhost:8000"


async def get_request_httpx(interaction: int, endpoint: str):
    async with httpx.AsyncClient(http2=True) as client:
        r = await client.get(f"{URL}/{endpoint}")
        print("httpx", f"interaction:{interaction}", r.text)


async def endpoint_1():
    """httpx example"""
    # tasks = []
    # for interaction in range(1000):
    #     tasks.append(asyncio.create_task(get_request_httpx(interaction, "page-1")))

    # await asyncio.gather(*tasks)

    # suspend control over coroutines outside of this context
    for interaction in range(1000):
        await asyncio.ensure_future(get_request_httpx(interaction, "page-1"))


async def get_request_aiohttp(interaction: int, endpoint: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}/{endpoint}") as response:
            r = await response.text()
            print("aiohttp", f"interaction:{interaction}", r)


async def endpoint_2():
    """aiohttp example"""
    # tasks = []
    # for interaction in range(1000):
    #     tasks.append(asyncio.create_task(get_request_aiohttp(interaction, "page-2")))

    # await asyncio.gather(*tasks)

    # suspend control over coroutines outside of this context
    for interaction in range(1000):
        await asyncio.ensure_future(get_request_aiohttp(interaction, "page-2"))


async def main():
    await asyncio.gather(endpoint_1(), endpoint_2())


if __name__ == "__main__":
    from time import time

    s = time()
    asyncio.run(main())
    e = time()
    print("execution time: ", e - s)
