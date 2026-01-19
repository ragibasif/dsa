#include <algorithm>
#include <iostream>
#include <list>
#include <map>
#include <stack>
#include <string>
#include <vector>
#include <sstream>
#include <utility>
#include <unordered_map>
#include <unordered_set>

using namespace std;
using ll = long long; 
using str = string; 
using pii = pair<int, int>; 
using pll = pair<ll, ll>; 
using vi = vector<int>; 
const int MOD = 1e9 + 7;

#ifndef DEBUG
#define DEBUG 0
#endif

#if DEBUG
#define dbg(x) cerr << "Line(" << __LINE__ << ") -> " << #x << " = " << (x) << endl;
#else
#define dbg(x)
#endif

#define IO(NAME) \
    ios_base::sync_with_stdio(false);\
    cin.tie(nullptr); cout.tie(nullptr);\
    if(fopen(NAME ".in","r")) freopen(NAME ".in","r",stdin), \
    freopen(NAME ".out","w",stdout); 

void solve() {
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr);

    IO("");


    int tc;
    cin >> tc;
    while (tc--) {
        solve();
    }

    return 0;
}


