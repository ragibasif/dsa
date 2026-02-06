#include <iostream>
#include <chrono>
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
using ull = unsigned long long;
using vi = vector<int>;
using vll = vector<ll>;
using vull = vector<ull>;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define all(x) (x).begin(), (x).end()
#define sz(x) static_cast<int>((x).size())
#define pb push_back

void solve() {
    ll n;
    cin >> n;
    unordered_set<ull> hash_set;
    hash_set.reserve((ull)n);
    ull val;
    while (cin>>val) {
	cin>>val;
	hash_set.insert(val);
    }
    cout << hash_set.size() << '\n';
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.tie(nullptr);

    int t = 1;
    //cin >> t; // multiple test cases
    while (t--) {
	auto start = chrono::steady_clock::now();
        solve();
	auto end = chrono::steady_clock::now();
	auto diff = chrono::duration_cast<chrono::milliseconds>(end-start);
	cerr << "Time: " << diff.count() << " ms" << endl;
    }
    return 0;
}

