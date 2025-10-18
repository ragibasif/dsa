

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

int solve( void ) {

    long long int n;
    if ( !( cin >> n ) ) { return EXIT_FAILURE; }

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
        chrono::duration<double, milli>( wc_end - wc_start ).count();
    cerr << "Finished in (Wall Clock): " << wc_elapsed_time_ms
         << " milliseconds." << endl;

    return EXIT_SUCCESS;
} // main
