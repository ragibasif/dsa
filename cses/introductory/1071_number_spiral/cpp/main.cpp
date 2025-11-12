/*
 * File: main.cpp
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: 1071 - number_spiral
 * Platform: cses
 * Difficulty: introductory
 * URL: https://cses.fi/problemset/task/1071
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
void print( const T &n ) {
    cerr << n << endl;
}

template <typename T1, typename T2>
void print( const pair<T1, T2> &n ) {
    cerr << "pair = [" << n.first << ", " << n.second << "]" << endl;
}

template <typename T>
void print( const vector<T> &n ) {
    cerr << "vector = [" << endl;
    bool first = true;
    for ( const auto &x : n ) {
        if ( !first ) { cerr << ", " << endl; }
        cerr << "    " << x;
        first = false;
    }
    cerr << endl << "]" << endl;
}

template <typename T>
void print( const unordered_set<T> &n ) {
    cerr << "unordered_set = {" << endl;
    bool first = true;
    for ( const auto &x : n ) {
        if ( !first ) { cerr << ", " << endl; }
        cerr << "    " << x;
        first = false;
    }
    cerr << endl << "}" << endl;
}

template <typename T1, typename T2>
void print( const unordered_map<T1, T2> &n ) {
    cerr << "unordered_map = {" << endl;
    bool first = true;
    for ( const auto &x : n ) {
        if ( !first ) { cerr << ", " << endl; }
        cerr << "    [" << x.first << ", " << x.second << "]";
        first = false;
    }
    cerr << endl << "}" << endl;
}

template <typename T>
T squared( T n ) {
    return n * n;
}

template <typename T>
bool is_even( T n ) {
    return n % 2 == 0;
}

template <typename T>
bool is_odd( T n ) {
    return n % 2 != 0;
}

} // namespace custom

using namespace custom;

/*----------------------------------------------------------------------------*/
// SOLVE
/*----------------------------------------------------------------------------*/

int solve( void ) {

    unsigned long long int y, x;
    if ( !( cin >> y ) || !( cin >> x ) ) { return EXIT_FAILURE; }

    // NOTE:
    // y = rows
    // x = cols
    // y axis has the even squares
    // x axis has the odd squares
    // if y gets even number, just square it
    // if y gets odd number, get square of y-1 and add 1 to it
    // if x gets odd number, just square it
    // if x gets even number, get square of x-1 and add 1 to it
    // if y gets even number, shifting right subtracts 1
    // if y gets odd number, shifting right adds 1
    // if x gets odd number, shifting down subtracts 1
    // if x gets even number, shifting down adds 1

    unsigned long long int y_modified;
    unsigned long long int x_modified;
    if ( is_even( y ) ) {
        y_modified = squared( y );
    } else {
        y_modified = squared( y - 1 ) + 1;
    }
    if ( is_odd( x ) ) {
        x_modified = squared( x );
    } else {
        x_modified = squared( x - 1 ) + 1;
    }

    unsigned long long int res;
    if ( y >= x && is_even( y ) ) {
        res = y_modified - ( x - 1 );
    } else if ( y > x && is_odd( y ) ) {
        res = y_modified + ( x - 1 );
    } else if ( x >= y && is_odd( x ) ) {
        res = x_modified - ( y - 1 );
    } else if ( x > y && is_even( x ) ) {
        res = x_modified + ( y - 1 );
    }

    cout << res << '\n';
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
    // t = 1;
    cin >> t; // Uncomment for multiple test cases
    for ( int i = 0; i < t; i++ ) {
        if ( solve() ) { break; }
    }

    cerr << endl
         << "Finished in " << clock() * 1.0 / CLOCKS_PER_SEC << " sec" << endl;

    return EXIT_SUCCESS;
} // main
