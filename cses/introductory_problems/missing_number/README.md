# introductory_problems_missing_number

Link: [introductory_problems_missing_number](https://cses.fi/problemset/task/1083)

- December 02, 2025 at 06:55 AM

```cpp
// time: O(N)
// space: O(1)
unsigned long long missing_number( unsigned long long n ) {
    // natural numbers
    // 1. get the sum of 1 to n natural numbers: ( n * ( n + 1 ) ) / 2;
    // 2. get the sum of input
    // 3. return the difference of step 1 and step 2
    unsigned long long sum_of_first_n = sum_of_first_n_natural_numbers( n );
    unsigned long long sum_of_input   = 0;
    for ( unsigned long long i = 0; i < n - 1; i++ ) {
        unsigned long long temp;
        std::cin >> temp;
        sum_of_input += temp;
    }
    return sum_of_first_n - sum_of_input;
}
```
