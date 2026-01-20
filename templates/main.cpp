#pragma GCC optimize("Ofast")
#pragma GCC target("avx,avx2,fma")

#include <iostream>
#include <cstdio>
#include <iomanip>
#include <sstream>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <unordered_set>
#include <unordered_map>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <complex>
#include <random>
#include <string>
#include <utility>
#include <tuple>
#include <chrono>
#include <bitset>
#include <functional>

using namespace std;

const int MOD = 1e9 + 7;

long long gcd(long long a, long long b) { return b == 0 ? a : gcd(b, a % b); }
long long lcm(long long a, long long b) { return b * (a / gcd(a, b)); }

#ifndef ONLINE_JUDGE
#define dbg(x) cerr << "Line(" << __LINE__ << ") -> " << #x << " = " << (x) << endl;
#else
#define dbg(x)
#endif

void solve() { 
    dbg("hello"); 
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);

    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif


    int t = 1; 
    //cin >> t;
    while (t--) {
        solve();
    }

    return 0;
}
