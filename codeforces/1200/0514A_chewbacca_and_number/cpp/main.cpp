/*
 * File: main.cpp
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: 0514A - chewbacca_and_number
 * Platform: codeforces
 * Difficulty: 1200
 * URL: https://codeforces.com/contest/514/problem/A
 */

/*----------------------------------------------------------------------------*/
// INCLUDES
/*----------------------------------------------------------------------------*/

#include <algorithm>
#include <bitset>
#include <cassert>
#include <chrono>
#include <climits>
#include <cmath>
#include <cstdint>
#include <functional>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <random>
#include <set>
#include <stack>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <vector>

using namespace std;

/*----------------------------------------------------------------------------*/
// FILE INPUT/OUTPUT
/*----------------------------------------------------------------------------*/

#define IO(NAME)                                                               \
    do {                                                                       \
        cin.tie(0)->sync_with_stdio(0);                                        \
        if (fopen(NAME ".in", "r")) {                                          \
            freopen(NAME ".in", "r", stdin);                                   \
            freopen(NAME ".out", "w", stdout);                                 \
        }                                                                      \
    } while (0)

/*----------------------------------------------------------------------------*/
// CONSTANTS
/*----------------------------------------------------------------------------*/

const int           MOD   = 1e9 + 7;
const int           INF   = 1e9;
const long long int LLINF = 4e18;
const double        PI    = acos(-1.0);
const int           dx[4]{1, 0, -1, 0}, dy[4]{0, 1, 0, -1};

/*----------------------------------------------------------------------------*/
// Debugging Helpers
/*----------------------------------------------------------------------------*/

template <typename T> void dbg(const T &n) { cerr << n << endl; }

template <typename T1, typename T2> void dbg(const pair<T1, T2> &n) {
    cerr << "pair = [" << n.first << ", " << n.second << "]" << endl;
}

template <typename T> void dbg(const vector<T> &n) {
    cerr << "vector = [" << endl;
    bool first = true;
    for (const auto &x : n) {
        if (!first) {
            cerr << ", " << endl;
        }
        cerr << "    " << x;
        first = false;
    }
    cerr << endl << "]" << endl;
}

template <typename T> void dbg(const unordered_set<T> &n) {
    cerr << "unordered_set = {" << endl;
    bool first = true;
    for (const auto &x : n) {
        if (!first) {
            cerr << ", " << endl;
        }
        cerr << "    " << x;
        first = false;
    }
    cerr << endl << "}" << endl;
}

template <typename T1, typename T2> void dbg(const unordered_map<T1, T2> &n) {
    cerr << "unordered_map = {" << endl;
    bool first = true;
    for (const auto &x : n) {
        if (!first) {
            cerr << ", " << endl;
        }
        cerr << "    [" << x.first << ", " << x.second << "]";
        first = false;
    }
    cerr << endl << "}" << endl;
}

/*----------------------------------------------------------------------------*/
// SOLVE
/*----------------------------------------------------------------------------*/

int solve(void) {

    long long int n;
    if (!(cin >> n)) {
        return EXIT_FAILURE;
    }

    long long int minx    = INT_MAX;
    long long int temp    = n;
    long long int counter = 0;
    while (temp) {
        int t = temp % 10;
        minx  = min(9 - t, t);
        if (!minx && !(temp / 10)) {
            minx = max(9 - t, t);
        }
        counter *= 10;
        counter += minx;
        temp /= 10;
    }

    long long int res = 0;
    while (n) {
        res *= 10;
        res += counter % 10;
        counter /= 10;
        n /= 10;
    }
    cout << res << endl;

    return EXIT_SUCCESS;
} // solve

/*----------------------------------------------------------------------------*/
// MAIN
/*----------------------------------------------------------------------------*/

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

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
