# introductory_problems_weird_algorithm

Link: [introductory_problems_weird_algorithm](https://cses.fi/problemset/task/1068/)

- December 02, 2025 at 06:49 AM

```cpp
// implementation of collatz conjecture
// time: O(N)
// space: O(1)
void weird_algorithm( long long n ) {
    std::cout << n << " ";
    while ( n != 1 ) {
        if ( is_even( n ) ) {
            n = n / 2;
        } else {
            n = n * 3 + 1;
        }
        std::cout << n << " ";
    }
    std::cout << "\n";
}
```

```cpp
// recursive implementation
// https://en.wikipedia.org/wiki/Collatz_conjecture
unsigned long long collatz_conjecture( unsigned long long n ) {
    std::cout << n << " ";
    if ( n == 1 ) {
        return 1;
    } // base case
    else if ( ( n & 1 ) == 0 ) { // even
        return collatz_conjecture( n / 2 );
    } else { // odd
        return collatz_conjecture( n * 3 + 1 );
    }
}

```
