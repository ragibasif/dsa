/*
 * File: main.cpp
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: 1092 - two_sets
 * Platform: cses
 * Difficulty: introductory
 * URL: https://cses.fi/problemset/task/1092
 */

/*----------------------------------------------------------------------------*/
// INCLUDES
/*----------------------------------------------------------------------------*/

// #include <algorithm>
// #include <bitset>
// #include <cassert>
// #include <chrono>
// #include <climits>
// #include <cmath>
// #include <cstdint>
// #include <functional>
#include <iostream>
// #include <iterator>
// #include <map>
// #include <numeric>
// #include <queue>
// #include <random>
// #include <set>
// #include <stack>
// #include <string>
// #include <tuple>
// #include <unordered_map>
// #include <unordered_set>
// #include <utility>
#include <vector>

using namespace std;

/*----------------------------------------------------------------------------*/
// FILE INPUT/OUTPUT
/*----------------------------------------------------------------------------*/

// #define USACO_IO(s)                                                            \
//     do {                                                                       \
//         freopen(((s) + ".in").c_str(), "r", stdin);                            \
//         freopen(((s) + ".out").c_str(), "w", stdout);                          \
//     } while (0)
//
// #define LOCAL_IO \
//     do { \
//         freopen("input.txt", "r", stdin); \
//         freopen("output.txt", "w", stdout); \
//     } while (0)

/*----------------------------------------------------------------------------*/
// CONSTANTS
/*----------------------------------------------------------------------------*/

// const int MOD = 1e9 + 7;
// const int INF = 1e9;
// const long long int LLINF = 4e18;
// const double PI = acos(-1.0);

/*----------------------------------------------------------------------------*/
// SOLVE
/*----------------------------------------------------------------------------*/

int solve(void) {

    long long int n;
    if (!(cin >> n)) {
        return EXIT_FAILURE;
    }
    long long int sum = (n * (n + 1)) / 2;
    if (n < 1 || sum % 2 != 0) {
        cout << "NO" << endl;
        return EXIT_SUCCESS;
    }

    long long int         sum_1 = 0;
    long long int         sum_2 = 0;
    vector<long long int> v1    = {};
    vector<long long int> v2    = {};

    for (int i = n; i > 0; i--) {
        if (sum_1 <= sum_2) {
            v1.push_back(i);
            sum_1 += i;
        } else {
            v2.push_back(i);
            sum_2 += i;
        }
    }

    if (sum_1 + sum_2 != sum) {
        cout << "NO" << endl;
        return EXIT_SUCCESS;
    }

    cout << "YES" << endl;
    cout << v1.size() << "\n";
    for (int i = 0; i < v1.size(); i++) {
        cout << v1[i] << " ";
    }
    cout << "\n" << v2.size() << "\n";
    for (int i = 0; i < v2.size(); i++) {
        cout << v2[i] << " ";
    }
    cout << "\n";

    return EXIT_SUCCESS;
} // solve

/*----------------------------------------------------------------------------*/
// MAIN
/*----------------------------------------------------------------------------*/

int main(void) {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

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
