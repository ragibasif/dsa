#!/usr/bin/env python3

import os
import sys
import time
from functools import wraps

def benchmark(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        wrapper.duration += end - start
        return res

    wrapper.calls = 0
    wrapper.duration = 0
    return wrapper


def report(func, res=None):
    if func.calls:
        print(f"Calls:  {func.calls}", file=sys.stderr)
    if func.duration:
        print(f"Time:  {func.duration:.6f}s", file=sys.stderr)
    if res:
        print(
            f"Memory: {sys.getsizeof(res) if res else 0} bytes (return val)",
            file=sys.stderr,
        )


def trace(func):
    level = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal level
        indent = "  | " * level
        arg_str = ", ".join(map(repr, args))
        print(f"{indent}+-- {func.__name__}({arg_str})", file=sys.stderr)
        level += 1
        res = func(*args, **kwargs)
        level -= 1
        print(f"{indent}+-- return {repr(res)}", file=sys.stderr)
        return res

    return wrapper


def inspect(obj):
    attrs = {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    print(f"object {type(obj).__name__}: {attrs}")


@benchmark
@trace
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    print(fib(6))
    report(fib)

if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
