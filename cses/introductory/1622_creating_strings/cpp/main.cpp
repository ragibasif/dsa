/*
 * File: main.cpp
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: 1622 - creating_strings
 * Platform: cses
 * Difficulty: introductory
 * URL: https://cses.fi/problemset/task/1622
 */

/*----------------------------------------------------------------------------*/
// INCLUDES
/*----------------------------------------------------------------------------*/

#include <algorithm>
// #include <bitset>
// #include <cassert>
#include <chrono>
// #include <climits>
#include <cmath>
// #include <cstdint>
// #include <functional>
#include <iostream>
// #include <iterator>
// #include <map>
// #include <numeric>
// #include <queue>
// #include <random>
#include <set>
// #include <stack>
#include <string>
// #include <tuple>
// #include <unordered_map>
// #include <unordered_set>
// #include <utility>
// #include <vector>

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
// SOLVE
/*----------------------------------------------------------------------------*/

set<string> hash_set;

void permutation( string prefix, string s ) {
    size_t n = s.size();
    if ( n == 0 ) {
        hash_set.insert( prefix );
    } else {
        for ( size_t i = 0; i < s.size(); i++ ) {
            permutation( prefix + s.at( i ),
                         s.substr( 0, i ) + s.substr( i + 1, s.size() ) );
        }
    }
}

int solve( void ) {

    // permutation problem
    // length: 1 <= n <= 8

    string str;

    if ( !( cin >> str ) ) { return EXIT_FAILURE; }

    // step 1: sort the input string in lexicographical order (non-decreasing)
    sort( str.begin(), str.end() );

    // try each character as the first char

    permutation( "", str );

    cout << hash_set.size() << "\n";
    for ( string key : hash_set ) { cout << key << "\n"; }

    return EXIT_SUCCESS;
} // solve

/*----------------------------------------------------------------------------*/
// MAIN
/*----------------------------------------------------------------------------*/

int main( void ) {
    // https://stackoverflow.com/questions/728068/how-to-calculate-a-time-difference-in-c/728070#728070
    auto wc_start = chrono::high_resolution_clock::now();

    ios_base::sync_with_stdio( false );
    cin.tie( NULL );
    cout.tie( NULL );

    IO( "string" );

    int t;
    t = 1;
    // cin >> t; // Uncomment for multiple test cases
    for ( int i = 0; i < t; i++ ) {
        if ( solve() ) { break; }
    }

    auto   wc_end = chrono::high_resolution_clock::now();
    double wc_elapsed_time_ms =
        chrono::duration<double, milli>( wc_end - wc_start ).count();
    cerr << "Finished in (Wall Clock): " << wc_elapsed_time_ms
         << " milliseconds." << endl;

    return EXIT_SUCCESS;
} // main
