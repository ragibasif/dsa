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
    string s;
    cin >>s;
    unordered_set<char> hashset;
    for (auto const c:s) {
	hashset.insert(c);
    }
    int n = sz(hashset);
    if ((n & 1 )== 1) { // odd, male
			//
	cout << "IGNORE HIM!" << '\n';
    } else {
	cout << "CHAT WITH HER!" << '\n';
    }
    
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

