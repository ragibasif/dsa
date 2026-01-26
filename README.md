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

### Math

- Sum of first `n` natural numbers: `( n * ( n + 1 ) ) / 2`
- Sum of first `n` odd natural numbers: `n * n`
- Sum of first `n` even natural numbers: `n * (n + 1)`
- Even number (`n = 2k`)
- Odd number (`n = 2k + 1`)

### Python

- Strings are immutable and that's why they can be used as keys to dictionaries
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
- `Counter`: frequency maps
- `deque`: O(1) append/pop from both ends (essential for BFS)
- `defaultdict`: avoids KeyError for graphs or counts
- Python's `heapq` is a min-heap by default. To use a max-heap, multiply values by `-1`.
- Tuples: are immutable, they can be used as keys to hash map/set
- Reverse a string: `s[::-1]`
- ASCII Conversion: `ord('a')` → 97, `chr(97)` → 'a'
- Infinity: `float('inf')` and `float('-inf')` or `math.inf` and `-math.inf`
- Divmod: `q, r = divmod(10, 3)` (Returns 3,1)

