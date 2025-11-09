/*----------------------------------------------------------------------------*/
// INCLUDES
/*----------------------------------------------------------------------------*/

// #include <algorithm>
// #include <bitset>
// #include <cassert>
#include <chrono>
#include <climits>
#include <cmath>
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

#define IO( NAME )                                                             \
    do {                                                                       \
        if ( fopen( NAME ".in", "r" ) ) {                                      \
            freopen( NAME ".in", "r", stdin );                                 \
            freopen( NAME ".out", "w", stdout );                               \
        }                                                                      \
    } while ( 0 )

/*----------------------------------------------------------------------------*/
// CONSTANTS
/*----------------------------------------------------------------------------*/

constexpr int           MOD     = 1e9 + 7;
constexpr int           INF     = 1e9;
constexpr double        EPSILON = 1e-9;
constexpr long long int LLINF   = 4e18;
const double            PI      = acos( -1.0 );
constexpr int           dx[4]{ 1, 0, -1, 0 }, dy[4]{ 0, 1, 0, -1 };

/*----------------------------------------------------------------------------*/
// HELPERS
/*----------------------------------------------------------------------------*/

template < typename T >
bool is_even( T n ) {
    return !( n & 1 );
}

template < typename T >
bool is_odd( T n ) {
    return n & 1;
}

bool is_eq_float( double a, double b ) { return abs( a - b ) < EPSILON; }

template < typename T >
T remainder( T x, T m ) {
    return x % m;
}

template < typename T >
T modulus( T x, T m ) {
    x = x % m;
    if ( x < 0 ) { x += m; }
    return x;
}

/*----------------------------------------------------------------------------*/
// SOLVE
/*----------------------------------------------------------------------------*/

// #include "dbg.h"
int solve() {
    // trailing zeros

    int n;
    if ( !( cin >> n ) ) { return EXIT_FAILURE; }

    long long int res = 0;

    // k = 1,2, ...,n
    // k x k
    // 2 knights
    // k choose 2
    // attack options: 2,3,4,6,8
    // (0,0),(0,n-1), (n-1,0), (n-1,n-1) = 2
    // (0,1),(1,0), (0,n-2),(n-2,0), (n-1,1), (1,n-1), (n-1,n-2), (n-2,n-1) = 3

    for ( long long int i = 1; i <= n; i++ ) {
        long long int size               = i * i; // k * k
        long long int knight1            = size;
        long long int knight2            = size - 1;
        long long int total_placements   = knight1 * knight2 / 2;
        long long int invalid_placements = 0;
        invalid_placements += 2 * ( 1 << 2 );     // 4 corners
        invalid_placements += 3 * ( 1 << 3 );     // 8 (2 per corner,adjacent)
        invalid_placements += 4 * ( 1 << 3 ) + 4; // 1 extra for each pair of 3s
        invalid_placements += 6 * ( 1 << 3 );     // none on first layer
        invalid_placements += 8 * ( 1 << 3 );     // none on first two layers
        long long int valid_placements = total_placements - invalid_placements;
        cout << valid_placements << '\n';
    }
    /*
       n = 1 * 1
       [[]]
       -> 0 (can't place both knights)
       n = 2 * 2
       [[],[],
       [],[]]
       -> 6 (n choose 2), no attacking
       n = 3 * 3
       [[2],[2],[2], 2 : 9
        [2],[2],[2],
        [2],[2],[2]]
       -> 28 (n choose 2)
      -  the elements are total possible attack options from that positions

       n = 4 * 4
       [[2],[3],[3],[2], 2 : 4
        [3],[4],[4],[3], 3 : 8
        [3],[4],[4],[3], 4 : 4
        [2],[3],[3],[2]]
        -> 96

        n = 5 * 5
       [[2],[3],[4],[3],[2], 2 : 4
        [3],[4],[6],[4],[3], 3 : 8
        [4],[6],[8],[6],[4], 4 : 8
        [3],[4],[6],[4],[3], 6 : 4
        [2],[3],[4],[3] [2]] 8 : 1
        -> 252
        - max attack options is 8
    */

    // cout << res;
    // cout << '\n';

    return EXIT_SUCCESS;
} // solve

/*----------------------------------------------------------------------------*/
// MAIN
/*----------------------------------------------------------------------------*/

int main() {
    // https://stackoverflow.com/questions/728068/how-to-calculate-a-time-difference-in-c/728070#728070
    auto wc_start = chrono::high_resolution_clock::now();

    // I/O is sometimes a bottleneck, the following makes it more efficient
    ios_base::sync_with_stdio( false );
    cin.tie( NULL );
    cout.tie( NULL );

    // IO( "test" );

    int t;
    t = 1; // Uncomment for single test case
    // cin >> t; // Uncomment for multiple test cases
    for ( int i = 0; i < t; i++ ) {
        if ( solve() ) { break; }
    }

    auto   wc_end = chrono::high_resolution_clock::now();
    double wc_elapsed_time_ms =
        chrono::duration< double, milli >( wc_end - wc_start ).count();
    cerr << "Finished in (Wall Clock): " << wc_elapsed_time_ms
         << " milliseconds." << endl;

    return EXIT_SUCCESS;
} // main
