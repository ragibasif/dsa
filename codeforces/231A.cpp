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
    int n;
    cin >>n;
    int counter = 0;
    while (n--) {
	int a,b,c;
	cin >> a >> b >> c;
	if ((a + b + c) >= 2) {
	    counter++;
	}
    }
    cout << counter << '\n';
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

