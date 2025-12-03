# introductory_problems_repetitions

Link: [introductory_problems_repetitions](https://cses.fi/problemset/task/1069/)

- December 02, 2025 at 07:54 AM

```cpp
unsigned long long repetitions( std::string_view line ) {
    // increment frequency while the chars are the same
    // reset the frequency to 1 if the chars are different
    // maintain running freq and max_freq
    char   prev     = line[0];
    int    max_freq = INT_MIN;
    size_t i        = 0;
    int    freq     = 0;
    while ( i < line.size() ) {
        if ( line[i] == prev ) {
            freq++;
        } else {
            freq = 1;
        }
        prev = line[i];
        i++;
        max_freq = std::max( max_freq, freq );
    }
    return max_freq;
}
```
