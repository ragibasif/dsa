# CPP

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
