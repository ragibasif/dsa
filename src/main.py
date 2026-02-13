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
import logging

logging.basicConfig(level=logging.DEBUG, format="[%(filename)s:%(lineno)d] %(message)s")
logger = logging.getLogger(__name__)


def log(*args):
    frame = inspect.currentframe().f_back
    var_names = inspect.getframeinfo(frame).code_context[0].strip()

    # Extract variable names from the log() call

    match = re.search(r"log\((.*)\)", var_names)
    if match:
        names = [n.strip() for n in match.group(1).split(",")]
        for name, value in zip(names, args):
            logger.debug(f"{name} = {value}")
    else:
        for i, value in enumerate(args):
            logger.debug(f"arg{i} = {value}")


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


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"

    def __str__(self):
        res = []
        curr = self
        seen = set()
        bound = 25

        while curr:
            node_id = id(curr)
            if node_id in seen:
                res.append(f"Cycle({curr.val})")
                break

            seen.add(node_id)
            res.append(str(curr.val))
            curr = curr.next

            if len(res) >= bound:
                res.append("...")
                break

        if not curr and len(res) < bound + 1:
            res.append("None")

        res = " -> ".join(res)
        return f"{res}"


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left_val = self.left.val if self.left else "null"
        right_val = self.right.val if self.right else "null"
        return f"TreeNode({self.val}, L:{left_val}, R:{right_val})"

    def __str__(self):
        lines = []

        def _build(node, prefix="", is_left=True, is_root=True):
            if node is None:
                label = "(L)" if is_left else "(R)"
                # Using \-- for bottom (left) and /-- for top (right)
                connector = "\\-- " if is_left else "/-- "
                lines.append(f"{prefix}{connector}{label} [N]")
                return

            if node.right or node.left:
                _build(
                    node.right,
                    prefix + ("|       " if is_left and not is_root else "        "),
                    False,
                    False,
                )

            if is_root:
                connector = "ROOT--- "
            else:
                label = "(L)" if is_left else "(R)"
                connector = "\\-- " if is_left else "/-- "
                connector += label + " "

            lines.append(f"{prefix}{connector}{node.val}")

            if node.left or node.right:
                _build(
                    node.left,
                    prefix + ("        " if is_left or is_root else "|       "),
                    True,
                    False,
                )

        _build(self)
        return "\n" + "\n".join(lines) + "\n"


@timer
@trace
@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def interval(arr1, arr2):
    pass


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
    x = 42
    y = [1, 2, 3]
    z = "hello"

    log(x)
    log(x, y, z)
    log(100)


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
