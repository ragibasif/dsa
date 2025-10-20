# Python

```python
import bisect  # bisect_left, bisect_right, insort
import collections  # Counter, defaultdict, deque, namedtuple
import functools
import heapq  # heapify, heappop, heappush, nlargest, nsmallest
import itertools
import math
import operator
import os
import random
import re
import string
import sys
```

## list

```python
arr = [1, 2, 3]
arr.append(4)      # add to end
arr.pop()          # remove last
arr.pop(0)         # remove first (O(n))
arr.insert(1, 99)  # insert at index
arr.remove(2)      # remove first occurrence
arr.clear()        # remove all
arr.sort()         # in-place sort
sorted(arr)        # returns new sorted list
arr.reverse()      # in-place reverse
arr.count(3)       # frequency of value
arr.index(3)       # find index
len(arr)           # length
```

- dynamic array, stack
- RAM, pop - O(1) time
- append - O(1) amortized time
- insert, remove, search - O(N)

## tuple

```python
t = (1, 2, 3)
len(t)
t[0]
x, y, z = t  # unpacking
```

- immutable

## set

```python

s = {1, 2, 3}
s.add(4)
s.remove(2)          # KeyError if not present
s.discard(5)         # no error if missing
s.pop()              # remove arbitrary element
s.clear()
s.union({4, 5})
s.intersection({2, 3, 4})
s.difference({1, 3})
3 in s               # membership test
```

- hash set
- unordered collection for unique elements
- O(1) time average

## dict

```python
d = {'a': 1, 'b': 2}
d['c'] = 3           # insert/update
d['a']               # access
d.get('x', 0)        # default value if missing
d.pop('b')           # remove key
'd' in d             # membership test
d.keys()
d.values()
d.items()
for k, v in d.items(): ...
len(d)

```

- hash table, key/value map
- access, insert, delete - O(1) average time

## collections.counter

```python
from collections import Counter

cnt = Counter(['a', 'b', 'a'])
cnt['a']        # 2
cnt.most_common(1)  # [('a', 2)]
cnt.update(['b', 'c'])
cnt.subtract(['a'])
```

- dictionary subclass
- frequency counting

## collections.defaultdict

```python
from collections import defaultdict

graph = defaultdict(list)
graph[0].append(1)
graph[0].append(2)
```

- dict with default values for missing keys

## collections.deque

```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
dq[0]; dq[-1]
```

- double-ended queue
- bfs
- append/pop from both ends - O(1) time

## heapq

```python
import heapq

# min-heap default

heap = [3, 1, 4]
heapq.heapify(heap)      # O(n)
heapq.heappush(heap, 2)
x = heapq.heappop(heap)
heap[0]                  # smallest element
heapq.nlargest(2, heap)
heapq.nsmallest(2, heap)

# use negatives to make max-heap

heapq.heappush(heap, -val)
-val = heapq.heappop(heap)
```

- priority queue
- min-heap implementation

## collections.OrderedDict

```python
from collections import OrderedDict
od = OrderedDict()
od['x'] = 1
od['y'] = 2
```

- preserves insertion order
- LRU cache

## collections.namedtuple

```python
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
p.x, p.y
```

## bisect

```python
import bisect

arr = [1, 3, 4, 4, 5]
i = bisect.bisect_left(arr, 4)  # first >= 4
j = bisect.bisect_right(arr, 4) # first > 4
bisect.insort(arr, 2)           # insert maintaining order
```

- binary search utilities for sorted lists

## string

```python
s = "hello world"
s.upper(); s.lower()
s.startswith("he")
s.endswith("ld")
s.split()
" ".join(['a', 'b'])
s.strip()
s.find("lo")
s.replace("l", "x")
```

## itertools

```python
import itertools

list(itertools.permutations([1,2,3]))
list(itertools.combinations([1,2,3], 2))
list(itertools.product([1,2], repeat=2))
itertools.accumulate([1,2,3])  # prefix sums
```

- combinatorics, generation, prefix sums
