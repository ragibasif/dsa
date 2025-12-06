# introductory_problems_gray_code

Link: [introductory_problems_gray_code](https://cses.fi/problemset/task/2205/)

- December 06, 2025 at 03:33 PM

```cpp

[[maybe_unused]] constexpr size_t        BITSET_MAX_SIZE = 64;

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
// Time: O(1)
// Space: O(1)
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
// Time: O(n)
// Space: O(n) if counting returned vector, O(1) otherwise
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
```
