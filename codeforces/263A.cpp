#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <numeric>
#include <cmath>
#include <bitset>
#include <unordered_set>

using namespace std;

using ll = long long;
using vi = vector<int>;
using vll = vector<ll>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define all(x) (x).begin(), (x).end()
#define sz(x) static_cast<int>((x).size())
#define pb push_back

void solve() {
    int N = 5;
    // center: (2,2), 12
    int r,c;
    for (int i = 0; i < N; i++) {
	for (int j = 0; j < N; j++) {
	    int temp;
	    cin >> temp;
	    if (temp) {
		r = i;
		c = j;
	    }
	}
    }
    cout << abs(r-2) + abs(c-2) << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    //cin >> t; // multiple test cases
    while (t--) {
        solve();
    }
    return 0;
}

