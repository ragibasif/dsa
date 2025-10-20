

/*----------------------------------------------------------------------------*/
// INCLUDES
/*----------------------------------------------------------------------------*/

// #include <algorithm>
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
// #include <set>
// #include <stack>
// #include <string>
// #include <tuple>
// #include <unordered_map>
#include <unordered_set>
// #include <utility>
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

constexpr int           MOD   = 1e9 + 7;
constexpr int           INF   = 1e9;
constexpr long long int LLINF = 4e18;
const double            PI    = acos( -1.0 );
constexpr int           dx[4]{ 1, 0, -1, 0 }, dy[4]{ 0, 1, 0, -1 };

/*----------------------------------------------------------------------------*/
// SOLVE
/*----------------------------------------------------------------------------*/

bool is_even( int n ) { return n % 2 == 0; }

// #include "dbg.h"
int solve( void ) {

    // a number should be distinct in its row and col
    // row[0] = 0 ... n-1
    // col[0] = 0 ... n-1

    /*
    In: 5

    Out:
    0 1 2 3 4
    1 0 3 2 5
    2 3 0 1 6
    3 2 1 0 7
    4 5 6 7 0
    */

    /*
    In: 10

    Out:
    0 1 2 3 4 5 6 7 8 9
    1 0 3 2 5 4 7 6 9 8
    2 3 0 1 6 7 4 5 10 11
    3 2 1 0 7 6 5 4 11 10
    4 5 6 7 0 1 2 3 12 13
    5 4 7 6 1 0 3 2 13 12
    6 7 4 5 2 3 0 1 14 15
    7 6 5 4 3 2 1 0 15 14
    8 9 10 11 12 13 14 15 0 1
    9 8 11 10 13 12 15 14 1 0
    */

    int n;
    if ( !( cin >> n ) ) { return EXIT_FAILURE; }

    vector< vector< int > > matrix( n, vector< int >( n ) );
    // dbg( matrix );

    /*
    0 1 2 3 4  \ 0 1 2 3 4  \  1 2 3 4
    1 0 3 2 5  \   0 3 2 5  \    3 2 5
    2 3 0 1 6  \     0 1 6  \      1 6
    3 2 1 0 7  \       0 7  \        7
    4 5 6 7 0  \         0
    */

    for ( int row = 0; row < n; row++ ) {
        for ( int col = 0; col < n; col++ ) {
            if ( row == col ) {
                matrix[row][col] = 0;
            } else if ( row == 0 ) {
                matrix[row][col] = col;
            } else if ( col == 0 ) {
                matrix[row][col] = row;
            } else {
                matrix[row][col] = 0;
            }
        }
    }

    for ( int row = 0; row < n; row++ ) {
        for ( int col = 0; col < n; col++ ) {
            if ( ( row == col ) || ( row == 0 ) || ( col == 0 ) ) {
                continue;
            } else {
                if ( is_even( row ) ) {
                    if ( is_even( col ) ) {
                        matrix[row][col] = row + col;
                    } else { // col is odd
                        matrix[row][col] = abs( row - col );
                    }
                } else { // row is odd
                    if ( is_even( col ) ) {
                        matrix[row][col] = row + col;
                    } else { // col is odd
                        matrix[row][col] = abs( row - col );
                    }
                }
            }
        }
    }

    for ( int row = 0; row < n; row++ ) {
        for ( int col = row + 1; col < n; col++ ) {
            matrix[col][row] = matrix[row][col];
        }
    }

    for ( const auto &row : matrix ) {
        for ( const auto &col : row ) { cout << col << " "; }
        cout << "\n";
    }

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

    // IO("");

    int t;
    t = 1;
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
