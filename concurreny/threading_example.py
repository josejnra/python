import asyncio
import concurrent.futures
import os
import threading


def blocking_io():
    # File operations (such as logging) can block the
    # event loop: run them in a thread pool.
    print("BLOCKING IO:", os.getpid(), threading.get_ident())
    with open("/dev/urandom", "rb") as f:
        return f.read(100)


def cpu_bound():
    # CPU-bound operations will block the event loop:
    # in general it is preferable to run them in a
    # process pool.
    print("CPU BOUND:", os.getpid(), threading.get_ident())
    return sum(i * i for i in range(10**7))


async def main():
    loop = asyncio.get_running_loop()

    ## Options:

    # 1. Run in the default loop's executor:
    result = await loop.run_in_executor(None, blocking_io)
    print("default thread pool", result)

    # 2. Run in a custom thread pool:
    with concurrent.futures.ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, blocking_io)
        # result = pool.submit(blocking_io)
        print("custom thread pool", result)

    # 3. Run in a custom process pool:
    with concurrent.futures.ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, cpu_bound)
        # result = pool.submit(cpu_bound)
        print("custom process pool", result)


asyncio.run(main())
