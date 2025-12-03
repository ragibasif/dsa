/*
 * File: main.cpp
 * Author: Ragib Asif
 * Email: ragibasif@tuta.io
 * GitHub: https://github.com/ragibasif
 * LinkedIn: https://www.linkedin.com/in/ragibasif/
 * SPDX-License-Identifier: MIT
 * Copyright (c) 2025 Ragib Asif
 * Version 1.0.0
 *
 * Description:
 *   Base C++ file for algorithm problems.
 *
 * Notes:
 *   - an n bit unsigned integer has a range of 0 to (2ⁿ)-1
 *   - an n bit signed integer has a range of -(2ⁿ⁻¹) to (2ⁿ⁻¹)-1
 *   - Bit masking is faster than modulus
 *   - Bit shifting is faster than multiplication/division
 *
 */

#include <algorithm> // sort, binary_search, lower_bound, shuffle
#include <bitset>    // bitset - for binary data
#include <cassert>   // assert - for debugging
#include <chrono>    // chrono::steady_clock, chrono::system_clock
#include <climits>   // INT_MAX, INT_MIN
#include <cmath>     // sqrt, pow, abs
#include <cstdint>   // int64_t, uint64_t, etc. fixed-width integer types
#include <fstream>
#include <functional> // greater, less, function objects and operations
#include <iostream>   // cout, cin, endl, Input/Output
#include <iterator>   // iterators and related items
#include <map>     // map, multimap, (non-hashed, tree) ordered key-value pairs
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

// using namespace std;
#define IO( NAME )                                                             \
    do {                                                                       \
        if ( fopen( NAME ".in", "r" ) ) {                                      \
            freopen( NAME ".in", "r", stdin );                                 \
            freopen( NAME ".out", "w", stdout );                               \
        }                                                                      \
    } while ( 0 )

[[maybe_unused]] constexpr int           MOD = static_cast< int >( 1e9 ) + 7;
[[maybe_unused]] constexpr int           INF = 1e9;
[[maybe_unused]] constexpr double        EPSILON = 1e-9;
[[maybe_unused]] constexpr long long int LLINF   = 4e18;
[[maybe_unused]] const double            PI      = acos( -1.0 );
[[maybe_unused]] constexpr int           dx[4]{ 1, 0, -1, 0 };
[[maybe_unused]] constexpr int           dy[4]{ 0, 1, 0, -1 };

// Euclidean Modulo
// In C/C++, a % b always returns results with the sign of a
// Mathematically, modulo is always non-negative
// % -> remainder operator in C
// % -> already behaves like Euclidean modulo for unsigned integers
// returns between [0,n-1], (same behavior of the modulo operator in python)
long long euclidean_modulo( long long a, long long b ) {
    if ( b == 0 ) { return 0; } // b == 0 is Undefined Behavior
    if ( a == INT_MIN && b == -1 ) {
        return 0;
    } // mathematically 0 but UB because of overflow
    long long r = a % b;
    if ( r < 0 ) {
        // these two lines are the same: (b > 0 ? : -b) == abs(b)
        // r += ( b > 0 ? b : -b );
        r += abs( b );
    }
    return r;
}

// recursive permutation
// n choose k: (n!) / (k!) * (n-k)!
unsigned long long combination( unsigned long long n, unsigned long long k ) {
    if ( n == 0 ) {
        return 1;
    } else if ( k == 0 ) {
        return 1;
    } else if ( n == k ) {
        return 1;
    } else {
        return combination( n - 1, k - 1 ) + combination( n - 1, k );
    }
}

// recursive factorial
// 0! = 1
// 1! = 1
// 2! = 2 * 1
// 5! = 5 * 4 * 3 * 2 * 1
unsigned long long factorial( unsigned long long n ) {
    if ( n == 0 || n == 1 ) { return 1; }
    return n * factorial( n - 1 );
}

// https://en.wikipedia.org/wiki/Summation
unsigned long long sum_of_first_n_natural_numbers( unsigned long long n ) {
    return ( n * ( n + 1 ) ) / 2;
}

unsigned long long sum_of_first_n_odd_natural_numbers( unsigned long long n ) {
    return n * n;
}

unsigned long long sum_of_first_n_even_natural_numbers( unsigned long long n ) {
    return n * ( n + 1 );
}

// recursive power
long double power( long double n, long double m ) {
    if ( m == 0 ) {
        return 1;
    } else if ( m > 0 ) {
        return n * power( n, m - 1 );
    } else {
        return 1 / power( n, std::abs( m ) );
    }
}

bool is_even( long long n ) { return ( n & 1 ) == 0; }
bool is_odd( long long n ) { return ( n & 1 ) == 1; }

int solve() {
    long long n; // int input
    if ( !( std::cin >> n ) ) { return EXIT_FAILURE; }
    // std::cout << n << "\n";

    // std::string line; // string input
    // if ( !( std::getline( std::cin >> std::ws, line ) ) ) {
    //     return EXIT_FAILURE;
    // }

    std::vector< unsigned long long > vec;
    for ( size_t i = 0; i < n; i++ ) {
        unsigned long long temp;
        std::cin >> temp;
        vec.push_back( temp );
    }

    return EXIT_SUCCESS;
}

int main( [[maybe_unused]] int argc, [[maybe_unused]] char **argv ) {
    // <https://stackoverflow.com/questions/728068/how-to-calculate-a-time-difference-in-c/728070#728070>
    auto wc_start = std::chrono::high_resolution_clock::now();

    // I/O is sometimes a bottleneck, the following makes it more efficient
    std::ios_base::sync_with_stdio( false );
    std::cin.tie( NULL );
    std::cout.tie( NULL );

    // IO( "test" );

    unsigned int test_cases;
    test_cases = 1; // Uncomment for single test case
    // std::cin >> t; // Uncomment for multiple test cases
    for ( unsigned int i = 0; i < test_cases; i++ ) {
        if ( solve() ) { break; }
    }
    std::cerr << std::endl;
    auto   wc_end = std::chrono::high_resolution_clock::now();
    double wc_duration =
        std::chrono::duration< double, std::milli >( wc_end - wc_start )
            .count();
    std::cerr << "[Wall Clock] Finished in: " << wc_duration << " milliseconds."
              << std::endl;
    return EXIT_SUCCESS;
}
