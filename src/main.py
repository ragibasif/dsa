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
import itertools
import inspect
from functools import cache, wraps
from types import GeneratorType

MOD: int = 10**9 + 7
EPS: float = 1e-9


class dbg:
    def __init__(self, *args):
        frame = inspect.currentframe().f_back
        info = inspect.getframeinfo(frame)
        names = {id(v): k for k, v in frame.f_locals.items()}

        for var in args:
            name = names.get(id(var), "Unknown")
            print(
                f"\nLine: {info.lineno} -> ({hex(id(var))}) {name}: {type(var).__name__} = {var}\n",
                file=sys.stderr,
            )

            if isinstance(var, (dict, Counter)):
                self._hashmap(var)

            elif isinstance(var, list) and var and isinstance(var[0], list):
                self._matrix(var)

            elif hasattr(var, "next"):
                self._sll(var)

            elif hasattr(var, "left") or hasattr(var, "right"):
                self._tree(var)

            else:
                print(f"  {var}", file=sys.stderr)

    def _hashmap(self, hashmap):
        print(f"  {'KEY':<15} | {'VALUE'}", file=sys.stderr)
        print(f"  {'-' * 30}", file=sys.stderr)
        try:
            items = sorted(hashmap.items())
        except TypeError:
            items = hashmap.items()
        for k, v in items:
            print(f"  {str(k):<15} | {v}", file=sys.stderr)

    def _matrix(self, matrix):
        if not matrix or not matrix[0]:
            print("  Empty {matrix}", file=sys.stderr)
            return
        width = 5
        R = len(matrix)
        C = len(matrix[0])

        print(f"\n({R}x{C})", file=sys.stderr)

        # Create Column Header (0, 1, 2...)
        col_header = " " * 5 + "".join(f"{c:>{width}}" for c in range(C))
        print(col_header, file=sys.stderr)
        print(" " * 4 + "+" + "-" * (C * width), file=sys.stderr)

        for r in range(R):
            row_str = f"{r:3d} |"
            for c in range(C):
                val = matrix[r][c]
                char = "." if val is None else str(val)
                if len(char) > width - 1:
                    char = char[: width - 2] + "+"
                row_str += f"{char:>{width}}"
            print(row_str, file=sys.stderr)
        print(" " * 4 + "+" + "-" * (C * width) + "\n", file=sys.stderr)

    def _sll(self, head):
        res = []
        curr = head
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
        print(f"  {res}", file=sys.stderr)

    def _tree(self, root):
        lines = []

        def _build(node, prefix="", is_left=True, is_root=True):
            if node is None:
                label = "(L)" if is_left else "(R)"
                # Using \-- for bottom (left) and /-- for top (right)
                connector = "  \\-- " if is_left else "  /-- "
                lines.append(f"{prefix}{connector}{label} [N]")
                return

            if node.right or node.left:
                _build(
                    node.right,
                    prefix
                    + ("  |       " if is_left and not is_root else "          "),
                    False,
                    False,
                )

            if is_root:
                connector = "  ROOT--- "
            else:
                label = "(L)" if is_left else "(R)"
                connector = "  \\-- " if is_left else "  /-- "
                connector += label + " "

            lines.append(f"{prefix}{connector}{node.val}")

            if node.left or node.right:
                _build(
                    node.left,
                    prefix + ("          " if is_left or is_root else "  |       "),
                    True,
                    False,
                )

        _build(root)
        print("\n" + "\n".join(lines) + "\n")


def trace(func):
    """Decorator to trace recursive functions."""
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


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        left_val = self.left.val if self.left else "null"
        right_val = self.right.val if self.right else "null"
        return f"TreeNode({self.val}, L:{left_val}, R:{right_val})"


@trace
@cache
def fib(n):
    if n <= 1:
        return 1
    return fib(n - 1) + fib(n - 2)


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

    my_dict = {"z": 1, "a": 10, "m": 5}
    my_counter = Counter("banana")

    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    head = ListNode(1, ListNode(2, ListNode(3)))
    head.next.next.next = head.next  # Creates cycle: 1 -> 2 -> 3 -> 2...

    root = TreeNode(
        10,
        left=TreeNode(5, left=TreeNode(2), right=TreeNode(7)),
        right=TreeNode(15, right=TreeNode(20)),
    )

    dbg(my_dict, my_counter, matrix, head, root)
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
            start = time.perf_counter()
            solve()
            end = time.perf_counter()
            print(f"Time: {end - start} seconds", file=sys.stderr)
            signal.alarm(0)  # Reset
    else:
        signal.alarm(2)  # Limit each test to 2 seconds
        start = time.perf_counter()
        solve()
        end = time.perf_counter()
        print(f"Time: {end - start} seconds", file=sys.stderr)
        signal.alarm(0)  # Reset


# region dbg


def _hashmap(hashmap):
    print(f"  {'KEY':<15} | {'VALUE'}", file=sys.stderr)
    print(f"  {'-' * 30}", file=sys.stderr)
    try:
        items = sorted(hashmap.items())
    except TypeError:
        items = hashmap.items()
    for k, v in items:
        print(f"  {str(k):<15} | {v}", file=sys.stderr)


def _matrix(matrix):
    if not matrix or not matrix[0]:
        print("  Empty {matrix}", file=sys.stderr)
        return
    width = 5
    R = len(matrix)
    C = len(matrix[0])

    print(f"\n({R}x{C})", file=sys.stderr)

    # Create Column Header (0, 1, 2...)
    col_header = " " * 5 + "".join(f"{c:>{width}}" for c in range(C))
    print(col_header, file=sys.stderr)
    print(" " * 4 + "+" + "-" * (C * width), file=sys.stderr)

    for r in range(R):
        row_str = f"{r:3d} |"
        for c in range(C):
            val = matrix[r][c]
            char = "." if val is None else str(val)
            if len(char) > width - 1:
                char = char[: width - 2] + "+"
            row_str += f"{char:>{width}}"
        print(row_str, file=sys.stderr)
    print(" " * 4 + "+" + "-" * (C * width) + "\n", file=sys.stderr)


def _sll(head):
    res = []
    curr = head
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
    print(f"  {res}", file=sys.stderr)


def _tree(root):
    lines = []

    def _build(node, prefix="", is_left=True, is_root=True):
        if node is None:
            label = "(L)" if is_left else "(R)"
            # Using \-- for bottom (left) and /-- for top (right)
            connector = "  \\-- " if is_left else "  /-- "
            lines.append(f"{prefix}{connector}{label} [N]")
            return

        if node.right or node.left:
            _build(
                node.right,
                prefix + ("  |       " if is_left and not is_root else "          "),
                False,
                False,
            )

        if is_root:
            connector = "  ROOT--- "
        else:
            label = "(L)" if is_left else "(R)"
            connector = "  \\-- " if is_left else "  /-- "
            connector += label + " "

        lines.append(f"{prefix}{connector}{node.val}")

        if node.left or node.right:
            _build(
                node.left,
                prefix + ("          " if is_left or is_root else "  |       "),
                True,
                False,
            )

    _build(root)
    print("\n" + "\n".join(lines) + "\n")


# endregion

# region fastio

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
atexit.register(sys.stdout.flush)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    main()
