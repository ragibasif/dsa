# Data Structures and Algorithms

## Notes

### Bit Manipulation

- Get i-th bit: `(x >> i) & 1`
- Set i-th bit: `x | (1 << i)`
- Clear i-th bit: `x & ~(1 << i)`
- Check if power of 2: `n > 0 and (n & (n - 1)) == 0`
- XOR Property: `a ^ a = 0`, `a ^ b = 1` if a != b
- Check if even number: `( n & 1 ) == 0`
- Check if odd number: `( n & 1 ) == 1`
- Clear the lowest set bit: `n & (n - 1)`
- Get the lowest set bit: `n & -n`

### Math

- Sum of first `n` natural numbers: `( n * ( n + 1 ) ) // 2`
- Sum of first `n` odd natural numbers: `n * n`
- Sum of first `n` even natural numbers: `n * (n + 1)`
- Even number: `n = 2k`
- Odd number: `n = 2k + 1`

### NP-Complete

- NP-Complete Problems:
  - Traveling Salesperson Problem (TSP)
  - Longest Path Problem
  - Hamiltonian Path Problem
  - Graph Coloring Problem
  - The Knapsack Problem
  - Subset Sum Problem

### Python

- Strings are immutable and that's why they can be used as keys to dictionaries
- Use `''.join(list_of_strings)` instead of repeated `s += char` since that will create new copies of the string
- For local documentation: use `help()` in the shell
- Use `enumerate()` to loop over a list to get the index and the item
- Get the key and the value when looping over a dictionary with `.items()`
- With a dictionary, if the value doesn't exist `[]` will throw a `KeyError` whereas
  `get()` will default to `None`
- `.sort()` sorts a list in place and `sorted()` returns a sorted _copy_ (uses Timsort)
- Sets are mutable, to get an immutable set that can be used for keys in dicts,
  use `frozenset`
- Deque - when you need a queue or list you can push and pop from either side
- Default Python recursion depth is about 1024 frames
- Infinity: `float("inf")`, `float("-inf")`, `math.inf`, `-math.inf`
- `Counter`: frequency maps `collections.Counter(arr)`
- `deque`: O(1) append/pop from both ends (essential for BFS)
- `defaultdict`: avoids KeyError for graphs or counts `collections.defaultdict(list)`
- Python's `heapq` is a min-heap by default. To use a max-heap, multiply values by `-1`.
- Tuples: are immutable, they can be used as keys to hash map/set
- Reverse a string: `s[::-1]`
- ASCII Conversion: `ord('a')` → 97, `chr(97)` → 'a'
- Infinity: `float('inf')` and `float('-inf')` or `math.inf` and `-math.inf`
- Divmod: `q, r = divmod(10, 3)` (Returns 3,1)
- GCD: `math.gcd(a,b)`
- LCM: `math.lcm(a,b)`
- Fast Power/Mod: `pow(base, exp, mod)` is faster than `(base**exp) % mod`
- Fast Grid Initialization: `grid = [[0 for _ in range(COLUMNS)] for _ in range(ROWS)]`
- nCr: `math.comb(n,r)`
- nPr: `math.perm(n,r)`
- Combinations: `itertools.combinations([1,2,3], 2)` → (1,2), (1,3), (2,3)
- Permutations: `itertools.permutations([1,2,3])`
- Integer Square Root: `math.isqrt(n)` is faster than `int(n**0.5)`
- Reverse a list: `list[::-1]`

### Utilities

Decorator to trace functions. Useful for recursive functions.

```python
from functools import wraps

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
```

Handle memoization with Python's built-in `@cache` decorator. It has no `maxsize` and will grow for as long as the program runs.

```python
from functools import cache

@cache
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

# Returns a named tuple showing hits, misses, and size.
info = fib.cache_info()
print(info)

# Deletes all cached results and resets statistics.
fib.cache_clear()
```

### 2D Arrays

Nested list comprehensions can be used to create a matrix with `ROWS` rows and `COLS` columns.

```python
matrix = [[0 for _ in range(COLS)] for _ in range(ROWS)]
visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
dist = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]
grid = [[(r * COLS + c) for c in range(COLS)] for r in range(ROWS)]
table = [[(i + 1) * (j + 1) for j in range(COLS)] for i in range(ROWS)]
```

Visualizes a 2D grid with row/column indices and fixed-width alignment. The width is the number of characters per cell.

```python
def debug_matrix(matrix,width=5):
    if not matrix or not matrix[0]:
        print(f"Empty", file=sys.stderr)
        return

    R = len(matrix)
    C = len(matrix[0])

    print(f"\n({R}x{C})", file=sys.stderr)

    # Create Column Header (0, 1, 2...)
    col_header = " " * 4 + "".join(f"{c:>{width}}" for c in range(C))
    print(col_header, file=sys.stderr)
    print(" " * 3 + "+" + "-" * (C * width), file=sys.stderr)

    for r in range(R):
        row_str = f"{r:2d} |"
        for c in range(C):
            val = matrix[r][c]
            char = "." if val is None else str(val)
            if len(char) > width - 1:
                char = char[:width-2] + "+"
            row_str += f"{char:>{width}}"
        print(row_str, file=sys.stderr)
    print(" " * 3 + "+" + "-" * (C * width) + "\n", file=sys.stderr)
```

### Singly-Linked Lists

Debug printing for singly-linked list. Detects cycles.

```python
def debug_sll(head):
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
```

### Trees

Print tree structure for debugging.

```python
def debug_tree(root):
    lines = []

    def build_line(node, prefix="", is_left=True, is_root=True):
        if node is None:
            label = "(L)" if is_left else "(R)"
            # Using \-- for bottom (left) and /-- for top (right)
            connector = "\\-- " if is_left else "/-- "
            lines.append(f"{prefix}{connector}{label} [N]")
            return

        if node.right or node.left:
            build_line(
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
            build_line(
                node.left,
                prefix + ("        " if is_left or is_root else "|       "),
                True,
                False
            )

    build_line(root)
    print("\n" + "\n".join(lines) + "\n")
```

Build a tree in level order from an array.

```python
def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root
```
