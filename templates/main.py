#!/usr/bin/env python3

import atexit
import os
import sys
from io import BytesIO, IOBase
import math
from collections import deque, defaultdict, Counter
import string
import time
import heapq
import itertools
from functools import cache, wraps

# --- CONSTANTS ---

MOD: int = 10**9 + 7
EPS: float = 1e-9
DEBUG: bool = os.path.exists("debug.txt")

# --- UTILITIES ---


def benchmark(func):
    if not DEBUG:
        return func

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
    if not DEBUG:
        return func
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
    if not DEBUG:
        return func
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
    """prints all non-private attributes of an object."""
    attrs = {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    print(f"object {type(obj).__name__}: {attrs}")



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"        

def dsll(head):
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
    print(res)

def arr_to_sll(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# --- SOLVE ---


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

    head = arr_to_sll([423,423,23,5,25,3,2,6,26,24232,62266])
    dsll(head)
    curr = head.next.next.next
    dummy = head
    while dummy.next:
        dummy = dummy.next
    dummy.next = curr
    
    dsll(head)


def main():
    flag: bool = False  # multiple test cases
    if flag:
        t = int(input())
        for _ in range(t):
            solve()
    else:
        solve()


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
if DEBUG:
    atexit.register(sys.stdout.flush)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
