# introductory_problems_increasing_array

Link: [introductory_problems_increasing_array](https://cses.fi/problemset/task/1094/)

- December 02, 2025 at 07:36 PM

```cpp
// check adjacent elements
// if prev element is greater than next element, add the difference to result
// time: O(N)
// space: O(1)
unsigned long long increasing_array( unsigned long long                n,
                                     std::vector< unsigned long long > vec ) {
    unsigned long long result = 0;
    for ( size_t i = 0; i < vec.size() - 1; i++ ) {
        if ( vec[i] > vec[i + 1] ) {
            unsigned long long temp = vec[i] - vec[i + 1];
            result += temp;
            vec[i + 1] += temp;
        }
    }
    return result;
}

```
