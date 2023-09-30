# memoization
# ensures that a function doesn’t run for the same inputs more than once by storing its result in memory and then referencing it later when necessary

# lru_cache (Least Recent Used) is one implementation of it


from functools import lru_cache


@lru_cache(maxsize=None)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    [fib(n) for n in range(20)]

    print(fib.cache_info())
