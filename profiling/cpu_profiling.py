import pstats
from cProfile import Profile

from line_profiler import LineProfiler
from pycallgraph2 import PyCallGraph
from pycallgraph2.output import GraphvizOutput


def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    profile = LineProfiler(fib(16))
    profile.print_stats()

    # another profiling option
    prof = Profile()
    prof.enable()
    fib(16)
    prof.disable()
    # print profiling output
    stats = pstats.Stats(prof).strip_dirs().sort_stats("cumtime")
    stats.print_stats(10)  # top 10 rows

    # another profiling option
    with PyCallGraph(output=GraphvizOutput()):
        fib(16)
