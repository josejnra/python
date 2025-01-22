from collections import deque
from queue import LifoQueue, Queue


def first_in_first_out():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)

    for i in q.queue:
        print(i)

    print(q.get())
    print(q.get())
    print(q.qsize())

    print("what is left:")
    for i in q.queue:
        print(i)

    print("final size:", q.qsize())
    print(q.get())
    print(q.empty())


def last_in_first_out():
    q = LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)

    for i in q.queue:
        print(i)
    print(q.get())
    print(q.get())
    print(q.qsize())


def deque_example():
    dq = deque()
    dq.append(1)
    dq.append(2)
    dq.append(3)

    print("Deque after appending elements:")
    for i in dq:
        print(i)

    print("Popped from right:", dq.pop())
    print("Popped from left:", dq.popleft())

    print("Deque after popping elements:")
    for i in dq:
        print(i)


if __name__ == '__main__':

    first_in_first_out()
    last_in_first_out()
    deque_example()
