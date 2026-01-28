# 10kgrind

![10kgrind](docs/10kgrind.png)

## Profiles

- [CSES](https://cses.fi/user/397111)
- [LeetCode](https://leetcode.com/u/10kgrind/)
- [Codeforces](https://codeforces.com/profile/10kgrind)

## Notes

![Flowchart](docs/dsa_flowchart.png)

### Asymptotic Complexity

![Big O](docs/dsa_big_o.png)

![Sorting Big O](docs/dsa_sorting_big_o.png)

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

- Sum of first `n` natural numbers: `( n * ( n + 1 ) ) / 2`
- Sum of first `n` odd natural numbers: `n * n`
- Sum of first `n` even natural numbers: `n * (n + 1)`
- Even number (`n = 2k`)
- Odd number (`n = 2k + 1`)

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
- Combinations: `itertools.combinations([1,2,3], 2)` → (1,2), (1,3), (2,3)
- Permutations: `itertools.permutations([1,2,3])`
- Integer Square Root: `math.isqrt(n)` is faster than `int(n**0.5)`
- Reverse a list: `list[::-1]`

### Snippets

Decorator to trace recursive functions

```py
from functools import wraps

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
```

Decorator for tracking call count and execution time

```py
import time

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
        print(f"Memory: {sys.getsizeof(res) if res else 0} bytes (return val)", file=sys.stderr)
```
