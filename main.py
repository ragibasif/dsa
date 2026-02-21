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
random.seed(SEED)


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

def _listnode(head:ListNode=None)->str:
    if not head:
        return "None"
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

def _treenode(root:TreeNode=None)->str:

    if not root:
        return "None"
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

    _build(root)
    return "\n" + "\n".join(lines) + "\n"

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b): return a * b // gcd(a, b)

def count_bits(x):
    bits = 0
    while x:
        bits += x & 1
        x >>= 1
    return bits

def count_set_bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

def is_even(x): return (x & 1) == 0
def is_odd(x): return (x & 1) != 0
def is_set(x, n): return (x & (1 << n)) == 1
def is_clear(x, n): return (x & (1 << n)) == 0
def get_bit(x, n): return (x >> n) & 1
def set_bit(x, n): return x | (1 << n)
def clear_bit(x, n): return x & ~(1 << n)
def toggle_bit(x, n): return x ^ (1 << n)
def clear_lowest_set_bit(x): return x & (x - 1)
def get_lowest_set_bit(x): return x & ~(x - 1)
def is_power_of_two(x): return x > 0 and clear_lowest_set_bit(x) == 0


def _bits(val,length=8):
    return f"{val:0>{length}b} ({val})"

def _matrix(grid, path=None):
    if not grid or not grid[0]: return ""

    path_set = set(path) if path else set()
    R, C = len(grid), len(grid[0])

    all_vals = []
    for row in grid:
        for val in row:
            all_vals.append(str(val))

    max_data_w = max(len(s) for s in all_vals)
    max_col_idx_w = len(str(C-1))
    cell_w = max(max_data_w, max_col_idx_w)
    full_cell_w = cell_w + 2
    row_idx_w = len(str(R-1))

    buf = []
    header_padding = " " * (row_idx_w + 3)
    header = header_padding + " ".join(str(c).center(full_cell_w) for c in range(C))
    buf.append(header)

    buf.append(" " * (row_idx_w + 2) + "-" * (len(header) - row_idx_w - 2))
    for r, row in enumerate(grid):
        line = []
        for c, val in enumerate(row):
            char = str(val)
            display = char.center(cell_w)
            if (r, c) in path_set:
                line.append(f"[{display}]")
            else:
                line.append(f" {display} ")
        buf.append(f"{str(r).rjust(row_idx_w)} | {' '.join(line)}")
    return "\n" + "\n".join(buf) + "\n"

@timer
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
    print(_bits(5))
    print(_bits(5^(-5)))
    print(_bits(5^(~5)))

    print(_bits(7))
    print(_bits(7^(-7)))
    print(_bits(7^(~7)))

    print(_bits(11))
    print(_bits(11^(-11)))
    print(_bits(11^(~11)))
    return

def random_integers(n, a, b):
    return [random.randint(a, b) for _ in range(n)]

def random_floats(n, a, b):
    return [random.uniform(a, b) for _ in range(n)]

def random_permutation(n):
    seq = list(range(1, n + 1))
    random.shuffle(seq)
    return seq

def random_matrix( n, m, a = 1, b = 10):
    m = m or n
    return [[random.randint(a, b) for _ in range(m)] for _ in range(n)]

def random_matrix_zero_diagonal( n, a= 1, b= 10):
    return [
            [0 if r == c else random.randint(a, b) for c in range(n)] for r in range(n)
            ]

def random_symmetric_matrix(  n, a= 1, b= 10):
    matrix = [[0] * n for _ in range(n)]
    for r in range(n):
        for c in range(r + 1):
            value = random.randint(a, b)
            matrix[r][c] = matrix[c][r] = value
    return matrix

def random_tree(n, depth: str = "shallow") -> list[tuple[int, int]]:
    """
    Generate random tree on n vertices (0 to n-1).
    depth: "shallow" (default), "deep", or "path"
    """
    if n <= 1:
        return []

    if depth == "path":
        alpha = 0
    elif depth == "deep":
        alpha = 3
    else:  # shallow
        alpha = n  # effectively random

    return [(random.randint(max(0, i - alpha), i), i + 1) for i in range(n - 1)]

def random_graph(n, connected = False) -> set[tuple[int, int]]:
    """
    Generate random graph on n vertices (0 to n-1).
    If connected=True, guarantees connectivity by including a random tree.
    """
    graph = {(i, j) for i in range(n) for j in range(i) if random.randint(0, 1)}

    if connected and n > 1:
        tree = set((min(u, v), max(u, v)) for u, v in self.random_tree(n))
        graph |= tree

    return graph

def random_string( n, charset= "ABCabc123"):
    """Generate random string of length n from given charset."""
    return "".join(random.choice(charset) for _ in range(n))

def random_string_uppercase(n): return "".join(random.choice(string.ascii_uppercase) for _ in range(n))
def random_string_lowercase(n): return "".join(random.choice(string.ascii_lowercase) for _ in range(n))
def random_string_alphanumeric( n): return "".join( random.choice(string.ascii_letters + string.digits) for _ in range(n))

def random_string_regex( n, pattern):
    """
    Generate random string matching regex pattern.
    Example: pattern = r"[A-Za-z0-9]"
    """
    regex = re.compile(pattern)
    charset = "".join(chr(c) for c in range(256) if regex.match(chr(c)))
    if not charset:
        raise ValueError(f"No characters match pattern: {pattern}")
    return "".join(random.choice(charset) for _ in range(n))

def format_matrix(matrix: List[List[int]], separator: str = " ") -> str:
    """Format matrix as string with rows on separate lines."""
    return "\n".join(separator.join(map(str, row)) for row in matrix)


def main():
    flag = False

    def handler(signum, frame):
        raise Exception("TLE: Test took too long!")

    signal.signal(signal.SIGALRM, handler)

    if flag:
        t = int(input())
        for _ in range(t):
            signal.alarm(2)
            solve()
            signal.alarm(0)
    else:
        signal.alarm(2)
        solve()
        signal.alarm(0)


if __name__ == "__main__":
    main()
