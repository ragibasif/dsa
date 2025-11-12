/*
 * File: main.cpp
 * Author: Ragib Asif
 * Email: ragib.asif30@myhunter.cuny.edu
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: 1069 - repetitions
 * Platform: cses
 * Difficulty: introductory
 * URL: https://cses.fi/problemset/task/1069
 */

/******************************************************************************/
/*                                  INCLUDES                                  */
/******************************************************************************/

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
#include <tuple>
#include <unordered_map> // unordered_map - hash map
#include <unordered_set> // unordered_set - hash set
#include <utility>       // pair
#include <vector>        // vector - dynamic array

using namespace std;

/******************************************************************************/
/*                                   INPUT                                    */
/******************************************************************************/

// #include "dbg.h" // comment out before submitting

#define FAST_IO                                                                \
    ios_base::sync_with_stdio(false);                                          \
    cin.tie(NULL);                                                             \
    cout.tie(NULL);

#define USACO_IO(s)                                                            \
    do {                                                                       \
        freopen(((s) + ".in").c_str(), "r", stdin);                            \
        freopen(((s) + ".out").c_str(), "w", stdout);                          \
    } while (0)

#define LOCAL_IO                                                               \
    do {                                                                       \
        freopen("input.txt", "r", stdin);                                      \
        freopen("output.txt", "w", stdout);                                    \
    } while (0)

/******************************************************************************/
/*                                 CONSTANTS                                  */
/******************************************************************************/

const int MOD = 1e9 + 7;
const int INF = 1e9;
const long long int LLINF = 4e18;
const double PI = acos(-1.0);

/******************************************************************************/
/*                                   SOLVE                                    */
/******************************************************************************/

int solve(void) {

    string str;
    cin >> str;
    size_t n = str.size();
    unsigned long long int max_ = 0;
    unsigned long long int curr_max = 0;
    char prev = '\0';

    for (size_t i = 0; i < n; i++) {
        if (!prev) {
            curr_max = 1;
            max_ = max(max_, curr_max);
        } else {
            if (prev == str[i]) {
                curr_max++;
                max_ = max(max_, curr_max);
            } else {
                curr_max = 1;
                max_ = max(max_, curr_max);
            }
        }
        prev = str[i];
    }
    if (curr_max < 1) {
        max_ = 1;
    }

    cout << max_ << '\n';
    return EXIT_SUCCESS;
} // solve

/******************************************************************************/
/*                    01101101 01100001 01101001 01101110                     */
/******************************************************************************/

int main(void) {
    FAST_IO;

#ifdef LOCAL
    LOCAL_IO;
#endif // LOCAL

#ifdef USACO
    USACO_IO("problem");
#endif // USACO

    int t;
    t = 1;
    // cin >> t; // Uncomment for multiple test cases
    for (int i = 0; i < t; i++) {
        if (solve()) {
            break;
        }
    }

    cerr << endl
         << "Finished in " << clock() * 1.0 / CLOCKS_PER_SEC << " sec" << endl;

    return EXIT_SUCCESS;
} // main
