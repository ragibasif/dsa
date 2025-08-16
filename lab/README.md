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

## Power Set

```c++
vector<int> subset;
int n = 3;

void generate_subsets(int k) {
    if (k == n + 1) {
        for (int i = 0; i < subset.size(); i++) {
            cout << subset[i] << " ";
        }
        cout << "\n";
    } else {
        // include k in the subset
        subset.push_back(k);
        generate_subsets(k + 1);
        subset.pop_back();
        // dont include k in the subset
        generate_subsets(k + 1);
    }
}

generate_subsets(1);

```

```sh
1 2 3
1 2
1 3
1
2 3
2
3
{}
```
