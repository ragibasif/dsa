#include <bits/stdc++.h>

using namespace std;

void solve() {
    long long n;
    cin >> n;
    long long expected = n * (n+1) / 2;
    for (int i = 0; i< n-1; i++) {
        long long temp;
        cin >> temp;
        expected -= temp;
    }
    cout << expected  << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}

