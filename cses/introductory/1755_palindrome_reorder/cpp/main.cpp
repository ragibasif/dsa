/*
 * File: main.cpp
 * Author: Ragib Asif
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Problem: 1755 - palindrome_reorder
 * Platform: cses
 * Difficulty: introductory
 * URL: https://cses.fi/problemset/task/1755
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
// Debugging Helpers
/*----------------------------------------------------------------------------*/

template <typename T>
void dbg( const T &n ) {
    cerr << n << endl;
}

template <typename T1, typename T2>
void dbg( const pair<T1, T2> &n ) {
    cerr << "pair = [" << n.first << ", " << n.second << "]" << endl;
}

template <typename T>
void dbg( const vector<T> &n ) {
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
void dbg( const unordered_set<T> &n ) {
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
void dbg( const unordered_map<T1, T2> &n ) {
    cerr << "unordered_map = {" << endl;
    bool first = true;
    for ( const auto &x : n ) {
        if ( !first ) { cerr << ", " << endl; }
        cerr << "    [" << x.first << ", " << x.second << "]";
        first = false;
    }
    cerr << endl << "}" << endl;
}

/*----------------------------------------------------------------------------*/
// SOLVE
/*----------------------------------------------------------------------------*/

bool same_chars( string input ) {
    for ( size_t i = 1; i < input.length(); i++ ) {
        if ( input[i] != input[i - 1] ) { return false; }
    }
    return true;
}

void fill_hashmap( string input, size_t input_length,
                   unordered_map<char, size_t> &hashmap ) {
    for ( size_t i = 0; i < input_length; i++ ) {
        auto it = hashmap.find( input[i] );
        if ( it == hashmap.end() ) { hashmap[input[i]] = 0; }
        hashmap[input[i]]++;
    }
}

bool valid_char_freq( bool is_even, unordered_map<char, size_t> &hashmap ) {
    if ( is_even ) {
        for ( auto &it : hashmap ) {
            if ( it.second % 2 != 0 ) { return false; }
        }
    } else {
        bool flag = true;
        for ( auto &it : hashmap ) {
            if ( it.second % 2 != 0 ) {
                if ( flag ) {
                    flag = false;
                } else {
                    return false;
                }
            }
        }
    }
    return true;
}

void output( string input, size_t input_length, bool is_even,
             unordered_map<char, size_t> &hashmap ) {
    size_t l = 0;
    size_t r = input_length - 1;
    while ( l < r ) {
        if ( is_even ) {
            for ( auto &it : hashmap ) {
                while ( it.second > 0 ) {
                    input[l++] = it.first;
                    it.second--;
                    input[r--] = it.first;
                    it.second--;
                }
            }
        } else {
            for ( auto &it : hashmap ) {
                if ( it.second % 2 != 0 ) {
                    input[input_length / 2] = it.first;
                    it.second--;
                }
                while ( it.second > 0 ) {
                    input[l++] = it.first;
                    it.second--;
                    input[r--] = it.first;
                    it.second--;
                }
            }
        }
    }
    cout << input << '\n';
}

int solve( void ) {

    string input;
    if ( !( cin >> input ) ) { return EXIT_FAILURE; }
    size_t input_length = input.length();
    bool   is_even      = input_length % 2 == 0;
    // all chars are the same -> solution
    if ( same_chars( input ) ) {
        cout << input << '\n';
        return EXIT_SUCCESS;
    }
    unordered_map<char, size_t> hashmap;
    fill_hashmap( input, input_length, hashmap );
    // if length parity is odd -> one unique char and even numbers of other
    // chars if length parity is even -> even numbers of all chars
    if ( !valid_char_freq( is_even, hashmap ) ) {
        cout << "NO SOLUTION\n";
        return EXIT_SUCCESS;
    }
    output( input, input_length, is_even, hashmap );

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
