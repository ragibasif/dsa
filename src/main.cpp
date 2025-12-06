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
[[maybe_unused]] constexpr size_t        BITSET_MAX_SIZE = 64;

long long euclidean_division( const long long a, const long long b );

// recursive permutation
// n choose k: (n!) / (k!) * (n-k)!
long long recursive_combination( const long long n, const long long k ) {
    if ( n == 0 ) {
        return 1;
    } else if ( k == 0 ) {
        return 1;
    } else if ( n == k ) {
        return 1;
    } else {
        return recursive_combination( n - 1, k - 1 ) +
               recursive_combination( n - 1, k );
    }
}

long long recursive_factorial( long long n );

// https://en.wikipedia.org/wiki/Summation
unsigned long long
sum_of_first_n_natural_numbers( const unsigned long long n ) {
    return ( n * ( n + 1 ) ) / 2;
}

unsigned long long
sum_of_first_n_odd_natural_numbers( const unsigned long long n ) {
    return n * n;
}

unsigned long long
sum_of_first_n_even_natural_numbers( const unsigned long long n ) {
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

long long                collatz( long long n );
std::vector< long long > collatz_sequence( long long n );

bool is_even( long long n );
bool is_odd( long long n );

class Graph {
    std::vector< std::vector< int > >          adjacency_list;
    std::vector< std::pair< int, int > >       adjacency_list_weighted;
    std::vector< std::vector< int > >          adjacency_matrix;
    std::vector< std::pair< int, int > >       edge_list;
    std::vector< std::tuple< int, int, int > > edge_list_weighted;

    std::vector< std::vector< int > > adj;
    std::vector< bool >               visited;
    // time: O( V + E)
    void dfs( int n ) {
        if ( visited[n] ) { return; }
        visited[n] = true;
        // process node n
        for ( auto u : adj[n] ) { dfs( u ); }
    }

    // time: O( V + E)
    void bfs( int n ) {
        std::vector< std::vector< int > > adj;
        std::vector< bool >               visited;
        std::vector< int >                distance;
        std::queue< int >                 q;
        visited[n]  = true;
        distance[n] = 0;
        q.push( n );
        while ( !q.empty() ) {
            int v = q.front();
            q.pop();
            // process node v
            for ( auto u : adj[v] ) {
                if ( visited[u] ) { continue; }
                visited[u]  = true;
                distance[u] = distance[v] + 1;
                q.push( u );
            }
        }
    }

    void bellman_ford( int n ) {
        std::vector< int >                         distance;
        std::vector< std::tuple< int, int, int > > edges;
        for ( int i = 0; i < n; i++ ) { distance[i] = INF; }
        distance[n] = 0;
        for ( int i = 0; i < n - 1; i++ ) {
            for ( auto e : edges ) {
                int u, v, w;
                std::tie( u, v, w ) = e; // tuple unpacking
                distance[v]         = std::min( distance[v], distance[u] + w );
            }
        }
    }
};

// XOR gate
// https://en.wikipedia.org/wiki/XOR_gate
// must have one or the other but not both
// 0 XOR 0 == 0
// 1 XOR 1 == 0
// 1 XOR 0 == 1
// 0 XOR 1 == 1
long long xor_gate( long long a, long long b ) { return a ^ b; }

// https://en.wikipedia.org/wiki/Gray_code
// https://cses.fi/problemset/task/2205
// Gray code
// 2:
//  00 -> 0 ^ (0 >> 1) -> 00 ^ 00
//  01 -> 1 ^ (1 >> 1) -> 01 ^ 00
//  11 -> 2 ^ (2 >> 1) -> 10 ^ 01
//  10 -> 3 ^ (3 >> 1) -> 11 ^ 01
// 3:
//  000
//  001
//  011
//  010
//  110
//  111
//  101
//  100
long long gray( long long n ) { return n ^ ( n >> 1 ); }
// constructing an n-bit gray code (recursive)
// to generate n bit gray code:
//  1. take n-1 bit gray code list
//  2. reflect the list (list entries in reverse order)
//  3. prefix entries of original list with a binary 0
//  4. prefix entries of reflected list with a binary 1
//  5. concatenate original list with the reverse list
// base case: 0 bits -> empty
// 1 bit -> (0,1)
std::vector< std::bitset< BITSET_MAX_SIZE > > gray_code( long long n ) {
    std::vector< std::bitset< BITSET_MAX_SIZE > > codes;
    if ( n <= 0 ) { return codes; } // base case, empty vector

    long long size = 1 << n; // 2ⁿ
    for ( long long i = 0; i < size; i++ ) {
        long long                      code = gray( i );
        std::bitset< BITSET_MAX_SIZE > item( code );
        codes.push_back( item );
    }
    return codes;
}

int solve() {
    long long n; // int input
    if ( !( std::cin >> n ) ) { return EXIT_FAILURE; }
    // std::cout << n << "\n";

    // std::string line; // string input
    // if ( !( std::getline( std::cin >> std::ws, line ) ) ) {
    //     return EXIT_FAILURE;
    // }

    std::vector< std::bitset< BITSET_MAX_SIZE > > gray_codes = gray_code( n );
    for ( auto item : gray_codes ) {
        if ( n < item.size() ) {
            std::string sub = item.to_string().substr( item.size() - n );
            std::cout << sub << "\n";
        } else {

            std::cout << item << "\n";
        }
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

    unsigned int cases;
    cases = 1; // Uncomment for single test case
    // std::cin >> cases; // Uncomment for multiple test cases
    for ( unsigned int i = 0; i < cases; i++ ) {
        if ( solve() ) { break; }
    }
    auto   wc_end = std::chrono::high_resolution_clock::now();
    double wc_duration =
        std::chrono::duration< double, std::milli >( wc_end - wc_start )
            .count();
    std::cerr << "\n[Wall Clock] Finished in: " << wc_duration
              << " milliseconds.\n"
              << std::flush;
    return EXIT_SUCCESS;
}

// https://en.wikipedia.org/wiki/Euclidean_division
// a = bq + r and 0 <= r < |b|
// euclidean modulo == euclidean division
// In C/C++, a % b always returns results with the sign of a
// Mathematically, modulo is always non-negative
// % -> remainder operator in C
// % -> already behaves like Euclidean modulo for unsigned integers
// returns between [0,n-1], (same behavior of the modulo operator in python)
long long euclidean_division( const long long a, const long long b ) {
    if ( b == 0 ) { // b == 0 is Undefined Behavior/Division by zero error
        return 0;
    }
    if ( a == INT_MIN && b == -1 ) {
        return 0; // mathematically 0 but UB because of overflow
    }
    long long r = a % b;
    if ( r < 0 ) { r += abs( b ); }
    return r;
}

// recursive factorial
// 0! = 1
// 1! = 1
// 2! = 2 * 1
// 5! = 5 * 4 * 3 * 2 * 1
long long recursive_factorial( long long n ) {
    if ( n <= 1 ) { return 1; }
    return n * recursive_factorial( n - 1 );
}

bool is_even( long long n ) { return ( n & 1 ) == 0; }

bool is_odd( long long n ) { return ( n & 1 ) == 1; }

// https://en.wikipedia.org/wiki/Collatz_conjecture
long long collatz( long long n ) {
    if ( ( n & 1 ) == 0 ) { // even
        return n / 2;
    }
    return n * 3 + 1; // odd
}

std::vector< long long > collatz_sequence( long long n ) {
    std::vector< long long > vec;
    long long                seq = n;
    vec.push_back( seq );
    while ( seq != 1 ) {
        seq = collatz( seq );
        vec.push_back( seq );
    }
    return vec;
}
