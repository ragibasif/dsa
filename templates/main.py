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


def report(func, res=None):
    if not DEBUG:
        return func
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


@benchmark
@cache
@trace
def fib(n, level=0):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
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
            
        return " -> ".join(res)

    def __repr__(self) -> str:
        return f"ListNode({self.val})"        

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        lines = []

        def build_tree_string(node, prefix="", is_left=True, is_root=True):
            if node is None:
                label = "(L)" if is_left else "(R)"
                # Using \-- for bottom (left) and /-- for top (right)
                connector = "\\-- " if is_left else "/-- "
                lines.append(f"{prefix}{connector}{label} [N]")
                return
            
            if node.right or node.left:
                build_tree_string(
                    node.right, 
                    prefix + ("|       " if is_left and not is_root else "        "), 
                    False, 
                    False
                )
            
            if is_root:
                connector = "ROOT--- "
            else:
                label = "(L)" if is_left else "(R)"
                connector = "\\-- " if is_left else "/-- "
                connector += label + " "
            
            lines.append(f"{prefix}{connector}{node.val}")
            
            if node.left or node.right:
                build_tree_string(
                    node.left, 
                    prefix + ("        " if is_left or is_root else "|       "), 
                    True, 
                    False
                )

        build_tree_string(self)
        return "\n" + "\n".join(lines) + "\n"

    def build(vals):
        if not vals: return None
        it = iter(vals)
        root = TreeNode(next(it))
        q = deque([root])
        while q:
            node = q.popleft()
            try:
                val = next(it)
                if val is not None:
                    node.left = TreeNode(val)
                    q.append(node.left)
                val = next(it)
                if val is not None:
                    node.right = TreeNode(val)
                    q.append(node.right)
            except StopIteration:
                break
        return root

class TrieNode:
    def __init__(self, char=""):
        self.char = char
        self.children = {}  # Map of char -> TrieNode
        self.is_end = False

    def __str__(self) -> str:
        lines = []

        def build_trie_string(node, prefix="", is_last=True):
            # Mark the node if it's the end of a word
            marker = "*" if node.is_end else ""
            display_char = node.char if node.char else "ROOT"
            
            # Draw the current node
            connector = "\\-- " if is_last else "|-- "
            lines.append(f"{prefix}{connector}{display_char}{marker}")

            # Prepare prefix for children
            new_prefix = prefix + ("    " if is_last else "|   ")
            
            # Sort children to keep output deterministic
            child_chars = sorted(node.children.keys())
            for i, char in enumerate(child_chars):
                is_last_child = (i == len(child_chars) - 1)
                build_trie_string(node.children[char], new_prefix, is_last_child)

        build_trie_string(self)
        return "\n".join(lines)

    def insert(root, word):
        curr = root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.is_end = True 


# --- SOLVE ---

@benchmark
@cache
@trace
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

# 1. Normal List: 1 -> 2 -> 3
    head = ListNode(1, ListNode(2, ListNode(3)))
    print("Normal", head)

# 2. Cyclic List: 1 -> 2 -> 3 -> (back to 2)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node2 # Creating the cycle

    print("Cyclic",node1)

    root = TreeNode(10)
    root.right = TreeNode(20, left=TreeNode(15))
    print(root)

    print(TreeNode.build([1, 2, 3, None, 4]))
    root = TrieNode()
    for w in ["cat", "cap", "can", "dog"]:
        TrieNode.insert(root, w)
    print(root)


def main():
    flag: bool = False  # multiple test cases
    if flag:
        t = int(input())
        for _ in range(t):
            solve()
    else:
        solve()
        report(solve)


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
