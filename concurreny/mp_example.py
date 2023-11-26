########################
# concurrent.futures
########################
import concurrent.futures
import time

import requests

URLS = ["https://example.com", "https://example.org", "https://example.net"]


def fetch(url):
    response = requests.get(url)
    return f"{url}: {response.status_code}"


def mp_main():
    """ "
    Provides a higher-level interface for asynchronous execution.
    It supports both asynchronous (via ThreadPoolExecutor and ProcessPoolExecutor) and synchronous execution.
    It's suitable for scenarios where tasks are I/O-bound (e.g., network requests, file I/O) and can benefit from concurrency.
    """
    with concurrent.futures.ProcessPoolExecutor() as executor:
        start_time = time.time()
        results = list(executor.map(fetch, URLS))
        end_time = time.time()

    for result in results:
        print(result)

    print(f"Time taken: {end_time - start_time} seconds")


# Define a simple function to be executed
def task(n):
    return n**2


def mp_future_main():
    # Create a ProcessPoolExecutor with maximum 2 worker processes
    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the executor
        results = [executor.submit(task, i) for i in range(5)]

        # Retrieve results as they become available
        for future in concurrent.futures.as_completed(results):
            result = future.result()
            print(result)


########################
# multiprocessing
########################

from multiprocessing import Manager, Pool, Process, Queue, set_start_method


def worker_function(worker_id: int, queue: Queue):
    result = f"Worker {worker_id} is done!"
    queue.put(result)


def cf_main():
    """
    Lower-level module that specifically focuses on parallelizing tasks using processes.
    It provides more manual control over processes and inter-process communication.
    It's specifically designed for parallelizing CPU-bound tasks.
    Since each process runs in its own Python interpreter, it can take full advantage of multi-core systems.
    """
    num_workers = 3
    results_queue = Queue()

    # Start worker processes
    processes = [Process(target=worker_function, args=(i, results_queue)) for i in range(num_workers)]
    start_time = time.time()

    for process in processes:
        process.start()

    # wait until completion
    for process in processes:
        process.join()

    # Retrieve results from the queue
    results = [results_queue.get() for _ in range(num_workers)]

    end_time = time.time()

    for result in results:
        print(result)

    print(f"Time taken: {end_time - start_time} seconds")


def cf_pool_main():
    """
    Uses a pool to manage the amount of process.
    """
    start_time = time.time()
    # set the fork start method
    # set_start_method("spawn")

    with Manager() as manager:
        # create the shared queue
        queue = manager.Queue()
        # create the pool of workers
        with Pool(processes=3) as pool:
            # calculations, 20 executions of the function
            params = [
                (
                    i,
                    queue,
                )
                for i in range(20)
            ]
            # execute the tasks in parallel
            pool.starmap(worker_function, params)

        end_time = time.time()
        print(f"Time taken: {end_time - start_time} seconds")

        # consume all items
        for _ in range(20):
            item = queue.get()
            print(item)


if __name__ == "__main__":
    mp_main()
    mp_future_main()
    cf_main()
    cf_pool_main()
