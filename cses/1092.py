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
from functools import cache, wraps

# --- CONSTANTS ---

MOD: int = 10**9 + 7
EPS: float = 1e-9
DEBUG: bool = os.path.exists("debug.txt")

# --- UTILITIES ---

def benchmark(func) :
    if not DEBUG: return func
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

def trace(func):
    if not DEBUG: return func
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

    return wrapper

def report(func,res=None):
    if not DEBUG: return func
    if func.calls:
        print(f"Calls:  {func.calls}", file=sys.stderr)
    if func.duration:
        print(f"Time:  {func.duration:.6f}s", file=sys.stderr)
    if res:
        print(f"Memory: {sys.getsizeof(res) if res else 0} bytes (return val)", file=sys.stderr)

def inspect(obj):
    """Prints all non-private attributes of an object."""
    attrs = {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    print(f"Object {type(obj).__name__}: {attrs}")

# --- SOLVE ---

@benchmark
@cache
@trace
def fib(n,level=0):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

def solve():
    # Read single integer
    # n = int(input())

    # Read multiple integers
    # n, m = map(int, input().split())

    # Read an array/list of integers
    # arr = list(map(int, input().split()))

    # Grid traversal
    # R, C = map(int, input().split())
    # grid = [input().strip() for _ in range(R)]

    # Your logic here

    n = int(input())
    s1 = 0
    arr1 = []
    s2 = 0
    arr2 = []
    for i in range(n,0,-1):
        if s1 >= s2:
            s2 += i
            arr2.append(str(i))
        else:
            s1 += i
            arr1.append(str(i))
    if s1 == s2:
        print("YES")
        print(len(arr1))
        print(" ".join(arr1))
        print(len(arr2))
        print(" ".join(arr2))
    else:
        print("NO")
    return 0
    

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
if DEBUG: atexit.register(sys.stdout.flush)
input = lambda: sys.stdin.readline().rstrip("\r\n")

# endregion

if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
