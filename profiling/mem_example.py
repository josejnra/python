def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    fib(1000)

    # memray run -o output.bin profiling/example.py
    # memray flamegraph output.bin

    # memray run --live profiling/example.py
