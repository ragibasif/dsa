#include <algorithm>
#include <bitset>
#include <chrono>
#include <cmath>
#include <iostream>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

using ll = long long;
using ull = unsigned long long;
using vi = vector<int>;
using vll = vector<ll>;
using vull = vector<ull>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define all(x) (x).begin(), (x).end()
#define sz(x) static_cast<int>((x).size())
#define pb push_back

bool is_even(ll n){ return (n&1) == 0;}
bool is_odd(ll n){ return (n&1) == 1;}

void solve() {
    ll y,x;
    cin >> y >> x;

    ll res = 1;

    if (y > x) {
	if (is_even(y)) {
	    res = (y*y) - x + 1;
	} else {
	    res = ((y-1) * (y-1)) + 1 + x - 1;
	}
    }
    else if (y < x) {
	if (is_odd(x)) {
	    res = (x*x) - y + 1;
	}else {
	    res = ((x-1) * (x-1)) + 1 + y - 1;
	}
    }
    else {
	if (is_even(y)) {
	    res = (y*y) - x + 1;
	} else {
	    res = (x*x) - y + 1;
	}
    }

    cout << res << '\n';

}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    cin >> t; // multiple test cases
    while (t--) {
	auto start = chrono::steady_clock::now();
	solve();
	auto end = chrono::steady_clock::now();
	auto diff = chrono::duration_cast<chrono::milliseconds>(end - start);
	cerr << "Time: " << diff.count() << " ms" << endl;
    }
    return 0;
}
