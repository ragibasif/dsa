#!/usr/bin/env python3


import signal
import atexit
import os
import sys
from io import BytesIO, IOBase
import math
import heapq
from collections import deque, defaultdict, Counter
import string
import time
import random
import re
import itertools
import inspect
from functools import cache, wraps
from types import GeneratorType
from typing import Final


MOD: Final[int] = 10**9 + 7
EPS: Final[float] = 1e-9
SEED: Final[int] = 69


def trace(func):
    """Decorator to trace recursive functions."""
    level = 0

    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal level
        indent = "  | " * level
        arg_str = ", ".join(map(repr, args))
        print(f"{indent}+-- {func.__name__}({arg_str})")
        level += 1
        res = func(*args, **kwargs)
        level -= 1
        print(f"{indent}+-- return {repr(res)}")
        return res

    return wrapper


def timer(func):
    """Decorator to time functions."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"[{func.__name__}] {duration:.4f}s ({duration * 1000:.2f}ms)")
        return result

    return wrapper


@trace
@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


@timer
def solve():
    """
    Read single integer:
    n = int(input())

    Read multiple integers:
    n, m = map(int, input().split())

    Read an array/list of integers:
    arr = list(map(int, input().split()))

    Grid traversal:
    R, C = map(int, input().split())
    grid = [input().strip() for _ in range(R)]
    """
    fib(6)


def main():
    flag: bool = False  # multiple test cases

    def handler(signum, frame):
        raise Exception("TLE: Test took too long!")

    signal.signal(signal.SIGALRM, handler)

    if flag:
        t = int(input())
        for _ in range(t):
            signal.alarm(2)  # Limit each test to 2 seconds
            solve()
            signal.alarm(0)  # Reset
    else:
        signal.alarm(2)  # Limit each test to 2 seconds
        solve()
        signal.alarm(0)  # Reset


if __name__ == "__main__":
    main()
