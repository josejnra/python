# Concurrency

**Parallelism** consists of performing multiple operations at the same time. Multiprocessing is a means to effect parallelism, and it entails spreading tasks over a computer’s central processing units (CPUs, or cores). Multiprocessing is well-suited for CPU-bound tasks: tightly bound for loops and mathematical computations usually fall into this category.

**Concurrency** is a slightly broader term than parallelism. It suggests that multiple tasks have the ability to run in an overlapping manner. (There’s a saying that concurrency does not imply parallelism.)

## Threading
Threading is a concurrent execution model whereby multiple threads take turns executing tasks. One process can contain multiple threads. Python has a complicated relationship with threading thanks to its GIL (Global Interpreter Lock) in the C implementation of python (CPython) . Python **threads** cannot take advantage of many cores. 

What’s important to know about threading is that it’s better for IO-bound tasks. While a CPU-bound task is characterized by the computer’s cores continually working hard from start to finish, an IO-bound job is dominated by a lot of waiting on input/output to complete.
To recap the above, concurrency encompasses both multiprocessing (ideal for CPU-bound tasks) and threading (suited for IO-bound tasks). Multiprocessing is a form of parallelism, with parallelism being a specific type (subset) of concurrency. The Python standard library has offered longstanding support for both of these through its *multiprocessing*, *threading*, and *concurrent.futures* packages.

## Async IO

Async functions need the ability to suspend and resume. A function that enters a waiting period is suspended, and only resumed when the wait is over. Four ways to implement suspend/resume in Python:
- Callback functions. A callback is a function that is passed as an argument to other function. This other function is expected to call this callback function in its definition. The point at which other function calls our callback function depends on the requirement and nature of other function.
- Generator functions
- Async/await (Python 3.5+)
- Greenlets (requires greenlet package)

Async functions enable you to write concurrent code using the `async/await` syntax. This powerful duo allows you to perform multiple tasks simultaneously without blocking the execution of your code. 🛠️ Think of it as having multiple browser tabs open; while one page loads, you can continue browsing other tabs. This capability means your Python applications can become faster, more efficient, and capable of handling many I/O operations.

`asyncio` library, which serves as a foundation for numerous asynchronous frameworks such as high-performance network and web servers, database connection libraries, and distributed task queues. 

The asyncio package is billed by the Python documentation as a library to write concurrent code. However, async IO is not threading, nor is it multiprocessing. It is not built on top of either of these.


Asyncio allows us to run IO-bound tasks asynchronously to increase the performance of our program. Common IO-bound tasks include calls to a database, reading and writing files to disk, and sending and receiving HTTP requests

In fact, async IO is a single-threaded, single-process design: it uses **cooperative multitasking**. It has been said in other words that async IO gives a feeling of concurrency despite using a **single thread** in a single process. Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent. To reiterate, async IO is a style of concurrent programming, but it is not parallelism. It’s more closely aligned with threading than with multiprocessing but is very much distinct from both of these and is a standalone member in concurrency’s bag of tricks.

### Example
Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.

Assumptions:

24 opponents
Judit makes each chess move in 5 seconds
Opponents each take 55 seconds to make a move
Games average 30 pair-moves (60 moves total)

- **Synchronous version**: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.
- **Asynchronous version**: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour.


### Scheduling Asynchronous Tasks
Async frameworks need a scheduler, usually called "event loop". The loop keeps track of all the running tasks. When a function is suspended, return controls to the loop, which then finds another function to start or resume. This is called **cooperative multi-tasking**.


### Async Function Without Await
It’s possible to create an async function without using the `await` keyword. However, without `await`, the async function becomes somewhat less useful, since you won’t be able to pause its execution and yield control back to the event loop. This means your async code will not be able to achieve cooperative concurrency, and other coroutines might be stuck waiting for their turn to execute. It’s generally a good idea to use `await` when working with async functions for more efficient asynchronous programming.


### When to use it


## Referencies
- [Async IO Python](https://realpython.com/async-io-python/)
- [Python Async Function](https://blog.finxter.com/python-async-function)
- [Making Concurrent HTTP requests with Python AsyncIO](https://www.laac.dev/blog/concurrent-http-requests-python-asyncio/)
- [Introdução à programação assíncrona em Python](https://medium.com/@edytarcio/async-await-introdu%C3%A7%C3%A3o-%C3%A0-programa%C3%A7%C3%A3o-ass%C3%ADncrona-em-python-fa30d077018e)
- [Miguel Grinberg Asynchronous Python for the Complete Beginner PyCon 2017](https://www.youtube.com/watch?v=iG6fr81xHKA&ab_channel=PyCon2017)
