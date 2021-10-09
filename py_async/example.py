import asyncio


async def do_something():
    for i in range(3):
        print(f'FROM task 1 there is {i}')
        await asyncio.sleep(1)


async def do_another_something():
    for i in range(2):
        print(f'FROM task 2 there is {i}')
        await asyncio.sleep(1)


async def main():
    r = await asyncio.gather(do_something(), do_another_something())
    print('Finished main function...')
    return r


if __name__ == '__main__':
    asyncio.run(main())
