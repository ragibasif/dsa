/*
 * File: main.cpp
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
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

#define IO( NAME )                                                             \
    do {                                                                       \
        cin.tie( 0 )->sync_with_stdio( 0 );                                    \
        if ( fopen( NAME ".in", "r" ) ) {                                      \
            freopen( NAME ".in", "r", stdin );                                 \
            freopen( NAME ".out", "w", stdout );                               \
        }                                                                      \
    } while ( 0 )

/*----------------------------------------------------------------------------*/
// CONSTANTS
/*----------------------------------------------------------------------------*/

const int           MOD   = 1e9 + 7;
const int           INF   = 1e9;
const long long int LLINF = 4e18;
const double        PI    = acos( -1.0 );
const int           dx[4]{ 1, 0, -1, 0 }, dy[4]{ 0, 1, 0, -1 };

/*----------------------------------------------------------------------------*/
// Custom Helpers
/*----------------------------------------------------------------------------*/

namespace custom {

template <typename T>
bool even( T n ) {
    return ( n & 1 ) == 0;
}

template <typename T>
bool odd( T n ) {
    return !even( n );
}

template <typename T>
class Subsets {
  private:
    vector<T> buffer;

  public:
    Subsets( T k ) {}
    ~Subsets() {}
};

} // namespace custom

/*----------------------------------------------------------------------------*/
// SOLVE
/*----------------------------------------------------------------------------*/

using namespace custom;

#include "dbg.h"

int solve( void ) {

    long long int n;
    if ( !( cin >> n ) ) { return EXIT_FAILURE; }

    return EXIT_SUCCESS;
} // solve

/*----------------------------------------------------------------------------*/
// MAIN
/*----------------------------------------------------------------------------*/

int main( void ) {
    ios_base::sync_with_stdio( false );
    cin.tie( NULL );
    cout.tie( NULL );

    int t;
    t = 1;
    // cin >> t; // Uncomment for multiple test cases
    for ( int i = 0; i < t; i++ ) {
        if ( solve() ) { break; }
    }

    cerr << endl
         << "Finished in " << clock() * 1.0 / CLOCKS_PER_SEC << " sec" << endl;

    return EXIT_SUCCESS;
} // main
