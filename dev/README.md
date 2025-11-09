# CPP

## Data Type Ranges

The Microsoft C++ 32-bit and 64-bit compilers recognize the types in the table later in this article.

```cpp
- int (unsigned int)
- __int8 (unsigned __int8)
- __int16 (unsigned __int16)
- __int32 (unsigned __int32)
- __int64 (unsigned __int64)
- short (unsigned short)
- long (unsigned long)
- long long (unsigned long long)
```

If its name begins with two underscores (`__`), the data type is nonstandard.

The ranges specified in the following table are inclusive-inclusive.

| Type Name                | Bytes                | Other Names                                          | Range of Values                                                                                                                  |
| ------------------------ | -------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| **`int`**                | 4                    | **`signed`**                                         | -2,147,483,648 to 2,147,483,647                                                                                                  |
| **`unsigned int`**       | 4                    | **`unsigned`**                                       | 0 to 4,294,967,295                                                                                                               |
| **`__int8`**             | 1                    | **`char`**                                           | -128 to 127                                                                                                                      |
| **`unsigned __int8`**    | 1                    | **`unsigned char`**                                  | 0 to 255                                                                                                                         |
| **`__int16`**            | 2                    | **`short`**, **`short int`**, **`signed short int`** | -32,768 to 32,767                                                                                                                |
| **`unsigned __int16`**   | 2                    | **`unsigned short`**, **`unsigned short int`**       | 0 to 65,535                                                                                                                      |
| **`__int32`**            | 4                    | **`signed`**, **`signed int`**, **`int`**            | -2,147,483,648 to 2,147,483,647                                                                                                  |
| **`unsigned __int32`**   | 4                    | **`unsigned`**, **`unsigned int`**                   | 0 to 4,294,967,295                                                                                                               |
| **`__int64`**            | 8                    | **`long long`**, **`signed long long`**              | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807                                                                          |
| **`unsigned __int64`**   | 8                    | **`unsigned long long`**                             | 0 to 18,446,744,073,709,551,615                                                                                                  |
| **`bool`**               | 1                    | none                                                 | **`false`** or **`true`**                                                                                                        |
| **`char`**               | 1                    | none                                                 | -128 to 127 by default<br /><br /> 0 to 255 when compiled by using [`/J`](../build/reference/j-default-char-type-is-unsigned.md) |
| **`signed char`**        | 1                    | none                                                 | -128 to 127                                                                                                                      |
| **`unsigned char`**      | 1                    | none                                                 | 0 to 255                                                                                                                         |
| **`short`**              | 2                    | **`short int`**, **`signed short int`**              | -32,768 to 32,767                                                                                                                |
| **`unsigned short`**     | 2                    | **`unsigned short int`**                             | 0 to 65,535                                                                                                                      |
| **`long`**               | 4                    | **`long int`**, **`signed long int`**                | -2,147,483,648 to 2,147,483,647                                                                                                  |
| **`unsigned long`**      | 4                    | **`unsigned long int`**                              | 0 to 4,294,967,295                                                                                                               |
| **`long long`**          | 8                    | none (but equivalent to **`__int64`**)               | -9,223,372,036,854,775,808 to 9,223,372,036,854,775,807                                                                          |
| **`unsigned long long`** | 8                    | none (but equivalent to **`unsigned __int64`**)      | 0 to 18,446,744,073,709,551,615                                                                                                  |
| **`enum`**               | varies               | none                                                 |                                                                                                                                  |
| **`float`**              | 4                    | none                                                 | 3.4E +/- 38 (seven digits)                                                                                                       |
| **`double`**             | 8                    | none                                                 | 1.7E +/- 308 (fifteen digits)                                                                                                    |
| **`long double`**        | same as **`double`** | none                                                 | Same as **`double`**                                                                                                             |
| **`wchar_t`**            | 2                    | **`__wchar_t`**                                      | 0 to 65,535                                                                                                                      |

A variable of **`__wchar_t`** designates either a wide-character type or multibyte-character type. Use the `L` prefix before a character or string constant to designate the wide-character-type constant.

**`signed`** and **`unsigned`** are modifiers that you can use with any integral type except **`bool`**. Note that **`char`**, **`signed char`**, and **`unsigned char`** are three distinct types for the purposes of mechanisms like overloading and templates.

The **`int`** and **`unsigned int`** types have a size of 4 bytes. However, portable code shouldn't depend on the size of **`int`** because the language standard allows this to be implementation-specific.

C/C++ in Visual Studio also supports sized integer types. For more information, see [`__int8, __int16, __int32, __int64`](../cpp/int8-int16-int32-int64.md) and [Integer Limits](../cpp/integer-limits.md).

For more information about the restrictions of the sizes of each type, see [Built-in types](../cpp/fundamental-types-cpp.md).

The range of enumerated types varies depending on the language context and specified compiler flags. For more information, see [C Enumeration Declarations](../c-language/c-enumeration-declarations.md) and [Enumerations](../cpp/enumerations-cpp.md).

## Built-in types (C++)

Built-in types (also called _fundamental types_) are specified by the C++ language standard and are built into the compiler. Built-in types aren't defined in any header file. Built-in types are divided into three main categories: _integral_, _floating-point_, and _void_. Integral types represent whole numbers. Floating-point types can specify values that may have fractional parts. Most built-in types are treated as distinct types by the compiler. However, some types are _synonyms_, or treated as equivalent types by the compiler.

## Void type

The [`void`](void-cpp.md) type describes an empty set of values. No variable of type **`void`** can be specified. The **`void`** type is used primarily to declare functions that return no values or to declare generic pointers to untyped or arbitrarily typed data. Any expression can be explicitly converted or cast to type **`void`**. However, such expressions are restricted to the following uses:

- An expression statement. For more information, see [Expressions](expressions-cpp.md).

- The left operand of the comma operator. For more information, see [Comma Operator](comma-operator.md).

- The second or third operand of the conditional operator (`? :`). For more information, see [Expressions with the Conditional Operator](conditional-operator-q.md).

## std::nullptr_t

The keyword **`nullptr`** is a null-pointer constant of type `std::nullptr_t`, which is convertible to any raw pointer type. For more information, see [`nullptr`](nullptr.md).

## Boolean type

The [`bool`](bool-cpp.md) type can have values [`true`](../cpp/true-cpp.md) and [`false`](../cpp/false-cpp.md). The size of the **`bool`** type is implementation-specific. See [Sizes of built-in types](#sizes-of-built-in-types) for Microsoft-specific implementation details.

## Character types

The **`char`** type is a character representation type that efficiently encodes members of the basic execution character set. The C++ compiler treats variables of type **`char`**, **`signed char`**, and **`unsigned char`** as having different types.

**Microsoft-specific**: Variables of type **`char`** are promoted to **`int`** as if from type **`signed char`** by default, unless the [`/J`](../build/reference/j-default-char-type-is-unsigned.md) compilation option is used. In this case, they're treated as type **`unsigned char`** and are promoted to **`int`** without sign extension.

A variable of type **`wchar_t`** is a wide-character or multibyte character type. Use the **`L`** prefix before a character or string literal to specify the wide-character type.

**Microsoft-specific**: By default, **`wchar_t`** is a native type, but you can use [`/Zc:wchar_t-`](../build/reference/zc-wchar-t-wchar-t-is-native-type.md) to make **`wchar_t`** a typedef for **`unsigned short`**. The **`__wchar_t`** type is a Microsoft-specific synonym for the native **`wchar_t`** type.

The **`char8_t`** type is used for UTF-8 character representation. It has the same representation as **`unsigned char`**, but is treated as a distinct type by the compiler. The **`char8_t`** type is new in C++20. **Microsoft-specific**: use of **`char8_t`** requires the [`/std:c++20`](../build/reference/std-specify-language-standard-version.md) compiler option or later (such as **`/std:c++latest`**).

The **`char16_t`** type is used for UTF-16 character representation. It must be large enough to represent any UTF-16 code unit. It's treated as a distinct type by the compiler.

The **`char32_t`** type is used for UTF-32 character representation. It must be large enough to represent any UTF-32 code unit. It's treated as a distinct type by the compiler.

## Floating-point types

Floating-point types use an IEEE-754 representation to provide an approximation of fractional values over a wide range of magnitudes. The following table lists the floating-point types in C++ and the comparative restrictions on floating-point type sizes. These restrictions are mandated by the C++ standard and are independent of the Microsoft implementation. The absolute size of built-in floating-point types isn't specified in the standard.

| Type              | Contents                                                                                                                                                      |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`float`**       | Type **`float`** is the smallest floating point type in C++.                                                                                                  |
| **`double`**      | Type **`double`** is a floating point type that is larger than or equal to type **`float`**, but shorter than or equal to the size of type **`long double`**. |
| **`long double`** | Type **`long double`** is a floating point type that is larger than or equal to type **`double`**.                                                            |

**Microsoft-specific**: The representation of **`long double`** and **`double`** is identical. However, **`long double`** and **`double`** are treated as distinct types by the compiler. The Microsoft C++ compiler uses the 4- and 8-byte IEEE-754 floating-point representations. For more information, see [IEEE floating-point representation](../build/ieee-floating-point-representation.md).

## Integer types

The **`int`** type is the default basic integer type. It can represent all of the whole numbers over an implementation-specific range.

A _signed_ integer representation is one that can hold both positive and negative values. It's used by default, or when the **`signed`** modifier keyword is present. The **`unsigned`** modifier keyword specifies an _unsigned_ representation that can only hold non-negative values.

A size modifier specifies the width in bits of the integer representation used. The language supports **`short`**, **`long`**, and **`long long`** modifiers. A **`short`** type must be at least 16 bits wide. A **`long`** type must be at least 32 bits wide. A **`long long`** type must be at least 64 bits wide. The standard specifies a size relationship between the integral types:

`1 == sizeof(char) <= sizeof(short) <= sizeof(int) <= sizeof(long) <= sizeof(long long)`

An implementation must maintain both the minimum size requirements and the size relationship for each type. However, the actual sizes can and do vary between implementations. See [Sizes of built-in types](#sizes-of-built-in-types) for Microsoft-specific implementation details.

The **`int`** keyword may be omitted when **`signed`**, **`unsigned`**, or size modifiers are specified. The modifiers and **`int`** type, if present, may appear in any order. For example, **`short unsigned`** and **`unsigned int short`** refer to the same type.

### Integer type synonyms

The following groups of types are considered synonyms by the compiler:

- **`short`**, **`short int`**, **`signed short`**, **`signed short int`**

- **`unsigned short`**, **`unsigned short int`**

- **`int`**, **`signed`**, **`signed int`**

- **`unsigned`**, **`unsigned int`**

- **`long`**, **`long int`**, **`signed long`**, **`signed long int`**

- **`unsigned long`**, **`unsigned long int`**

- **`long long`**, **`long long int`**, **`signed long long`**, **`signed long long int`**

- **`unsigned long long`**, **`unsigned long long int`**

**Microsoft-specific** integer types include the specific-width **`__int8`**, **`__int16`**, **`__int32`**, and **`__int64`** types. These types may use the **`signed`** and **`unsigned`** modifiers. The **`__int8`** data type is synonymous with type **`char`**, **`__int16`** is synonymous with type **`short`**, **`__int32`** is synonymous with type **`int`**, and **`__int64`** is synonymous with type **`long long`**.

## Sizes of built-in types

Most built-in types have implementation-defined sizes. The following table lists the amount of storage required for built-in types in Microsoft C++. In particular, **`long`** is 4 bytes even on 64-bit operating systems.

| Type                                                                                                       | Size    |
| ---------------------------------------------------------------------------------------------------------- | ------- |
| **`bool`**, **`char`**, **`char8_t`**, **`unsigned char`**, **`signed char`**, **`__int8`**                | 1 byte  |
| **`char16_t`**, **`__int16`**, **`short`**, **`unsigned short`**, **`wchar_t`**, **`__wchar_t`**           | 2 bytes |
| **`char32_t`**, **`float`**, **`__int32`**, **`int`**, **`unsigned int`**, **`long`**, **`unsigned long`** | 4 bytes |
| **`double`**, **`__int64`**, **`long double`**, **`long long`**, **`unsigned long long`**                  | 8 bytes |

See [Data type ranges](data-type-ranges.md) for a summary of the range of values of each type.

For more information about type conversion, see [Standard conversions](standard-conversions.md).

## See also

[Data type ranges](data-type-ranges.md)

/_----------------------------------------------------------------------------_/
// NOTES
/_----------------------------------------------------------------------------_/

/\*

- int -> 32 bits -> -2^31 ... 2^31 - 1 (about -2*10^9 ... 2*10^9)
- long long -> 64 bits -> -2^63 ... 2^63 - 1 (about -9*10^18 ... 9*10^18)
- double -> 64 bits
-
-
- mod - x mod m is the remainder when x is divided by m (17 mod 5 = 2)
- (a+b) mod m = (a mod m + b mod m) mod m
- (a-b) mod m = (a mod m - b mod m) mod m
- (a*b) mod m = (a mod m * b mod m) mod m
- want remainder to be between 0 and m - 1, but in cpp the remainder of a
- negative number is either zero or negative, to counteract this, first get the
- remainder and add m to it if the result is negative
-
-
- floating point numbers - some numbers cannot be represented accurately with
- floating point numbers and there will be rounding errors its risky to compare
- floating point numbers with == because its likely they should be equal but
- are not due to precision errors to compare floating point numbers: assume the
- two numbers are equal if the difference between them is less than epsilon
-
- exponential notation
- e - "times 10-to-the-power-of"
- 1e-9 == 0.000000001; minus sign applies to the exponent
- -1e9 == -1000000000.0; minus sign applies to the constant 1
-
- '\n' is faster than endl because 'endl' causes a flush operation
  \*/

/_----------------------------------------------------------------------------_/

---

```c++
#include <algorithm>  // sort, binary_search, lower_bound, upper_bound, shuffle
#include <bitset>     // bitset - for binary data
#include <cassert>    // assert - for debugging
#include <chrono>     // chrono::steady_clock, chrono::system_clock
#include <climits>    // INT_MAX, INT_MIN
#include <cmath>      // sqrt, pow, abs
#include <cstdint>    // int64_t, uint64_t, etc. - fixed-width integer types
#include <functional> // greater, less - function objects and operations
#include <iostream>   // cout, cin, endl - Input/Output
#include <iterator>   // iterators and related items
#include <map>     // map, multimap - (non-hashed, tree) ordered key-value pairs
#include <numeric> // accumulate, gcd, lcm - numeric operations
#include <queue>   // queue, priority_queue
#include <random>  // mt19937, mt19937_64 (higher quality RNG than rand())
#include <set>     // set, multiset - (non-hashed, tree) ordered set
#include <stack>   // stack
#include <string>  // string
#include <tuple>   // tuple
#include <unordered_map> // unordered_map - hash map
#include <unordered_set> // unordered_set - hash set
#include <utility>       // pair
#include <vector>        // vector - dynamic array
```

## vector<T>

```cpp
vector<int> v = {1, 2, 3};
v.push_back(4);      // append
v.pop_back();        // remove last
v.size();            // number of elements
v.empty();           // check if empty
v.clear();           // remove all
v.front(); v.back(); // access ends
v[i];                // random access
v.begin(), v.end();  // iterators
sort(v.begin(), v.end()); // sort
reverse(v.begin(), v.end());
```

- dynamic arrays
- random access: O(1)
- push_back: O(1) amortized

## array<T, N>

```cpp
array<int, 3> arr = {1, 2, 3};
arr.fill(0); arr.size(); arr.front(); arr.back();
```

- fixed-size array

## deque<T>

```cpp
deque<int> dq;
dq.push_back(1); dq.push_front(2);
dq.pop_back(); dq.pop_front();
dq.front(); dq.back();
```

- double-ended queue
- BFS, sliding window, monotonic queues

## stack<T>

```cpp

stack<int> st;
st.push(1); st.pop();
st.top(); st.empty();

```

- DFS, monotonic stack, parentheses problems

## queue<T>

```cpp

queue<int> q;
q.push(1); q.pop();
q.front(); q.empty();
```

- BFS traversal, task scheduling

## priority_queue<T>

```cpp

// default: max-heap
priority_queue<int> pq;
pq.push(3); pq.push(1);
pq.top(); pq.pop();

// min-heap
priority_queue<int, vector<int>, greater<int>> minpq;
```

- Dijkstra, top-K problems, greedy algorithm

## set<T> / multiset<T>

- sorted unique container
- O(log N) operations

```cpp
set<int> s;
s.insert(3); s.erase(3);
s.count(3); // 0 or 1
s.find(3);
```

- `multiset` allows duplicates
- maintaining sorted order, median tracking, removing elements efficiently

## unordered_set<T>

- hash-based
- unsorted
- O(1) average operations

```cpp
unordered_set<int> us;
us.insert(3); us.erase(3);
us.count(3);
```

- fast membership check, duplicates removal

## map<K, V> / unordered_map<K, V>

```cpp
map<int, string> mp;                // ordered
unordered_map<int, string> ump;     // faster, no order

mp[1] = "A"; ump[2] = "B";
mp.count(1); mp.find(2);
mp.erase(1);
for (auto &[k, v] : mp) cout << k << " " << v;
```

- frequency counting, lookups, memoization

## pair<T1, T2> and tuple<T1, T2, T3>

- small fixed groupings of data

```cpp

pair<int, int> p = {1, 2};
p.first;
p.second;

tuple<int, string, double> t = {1, "hi", 3.14};
get<0>(t);
```

## string

- dynamic character array

```cpp

string s = "hello";
s.size();
s.empty();
s.push_back('!');
s.pop_back();
s.substr(1, 3);
s.find("ll"); // returns index or npos
reverse(s.begin(), s.end());
```

- substrings, string parsing, manipulation

## bitset<N>

- fixed-size array of bits

```cpp

bitset<8> b("1010");
b.count();
b.any();
b.none();
b.set(2);
b.reset(2);
b.flip();
b.to_ulong();
```

- bitmask DP, subset enumeration, flags

## list<T> / forward_list<T>

- doubly and singly linked lists

```cpp
list<int> l;
l.push_back(1);
l.push_front(2);
l.pop_back();
l.pop_front();
```

- LRU cache

## Common STL Algorithms

```cpp
sort(v.begin(), v.end());
reverse(v.begin(), v.end());
accumulate(v.begin(), v.end(), 0);
max_element(v.begin(), v.end());
min_element(v.begin(), v.end());
count(v.begin(), v.end(), val);
find(v.begin(), v.end(), val);
lower_bound(v.begin(), v.end(), val);
upper_bound(v.begin(), v.end(), val);
unique(v.begin(), v.end());
```

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
