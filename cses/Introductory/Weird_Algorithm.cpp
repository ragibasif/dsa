#include <bits/stdc++.h>

using namespace std;

void solve() {
    long long n;
    cin >> n;
    cout << n << " ";
    while (n > 1) {
        if ((n & 1) == 0){ // even
            n /= 2;
        } else {
            n *= 3;
            n++; 
        }
        cout << n << " ";
    }
    cout << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}



