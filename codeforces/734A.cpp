#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <climits>
#include <cctype>
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

using ll = long long;
using ull = unsigned long long;
using ld = long double;
using pii = pair<int,int>;
using pll = pair<ll,ll>;
using vi = vector<int>;
using vll = vector<ll>;
using str = string;

#define all(x) (x).begin(), (x).end()
#define sz(x) ((int)(x).size())
#define pb push_back
#define mp make_pair
#define mt make_tuple
#define eb emplace_back
#define fi first
#define se second

[[maybe_unused]]const ll MOD = 1e9 + 7;
[[maybe_unused]]const int INF = 1e9;
[[maybe_unused]]const ll LLINF = 1e18;
[[maybe_unused]]const ld EPS = 1e-9;
[[maybe_unused]]const ld PI = acos(-1);

/** 
 
int month[]={-1,31,28,31,30,31,30,31,31,30,31,30,31};  //Not Leap Year 
 
int dx[]={1,0,-1,0}; 
int dy[]={0,1,0,-1}; //4 Direction 
 
int dx[]={1,1,0,-1,-1,-1,0,1}; 
int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction 
 
int dx[]={2,1,-1,-2,-2,-1,1,2}; 
int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction (horse) 
 
**/ 
const int dx4[] = {-1, 0, 1, 0}; 
const int dy4[] = { 0, 1, 0,-1}; 
 
const int dx8[] = {-1, 0, 1, 0, -1,-1, 1, 1}; 
const int dy8[] = { 0, 1, 0,-1, -1, 1,-1, 1}; 

bool is_even(ll n) { return (n & 1) == 0; }
bool is_odd(ll n) { return (n & 1) != 0; }


ll mod(ll a, ll b) { if ( b == 0 || ( a == LLONG_MIN && b == -1 )) { return 0; } ll r = a % b; if ( r < 0 ) { r += llabs( b ); } return r; }
ll gcd(ll a, ll b) { while (b) { ll c = a; a = b; b = mod(c,b); } return a; }
ll lcm(ll a, ll b) { return b * (a / gcd(a, b)); }

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
template<typename... T> void _dbg(T... args) { ((cerr << args << " "), ...); cerr << endl; }

#ifdef LOCAL
#define dbg(...) cerr << "LINE(" << __LINE__ << ") -> [" << #__VA_ARGS__ << "]: ", _dbg(__VA_ARGS__)
#else
#define dbg(...)
#endif

void solve() {
    int n;
    cin >> n;
    str s;
    cin >> s;
    int a=0;
    int d=0;
    for (auto const c:s) {
	if (c == 'A') {
	    a++;
	} else{
	    d++;
	}
    }

    if (a > d) {
	cout << "Anton" << '\n';
    } else if (a < d) {
	cout << "Danik" << '\n';
    } else {
	cout << "Friendship" << '\n';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cin.tie(nullptr);

    #ifdef LOCAL
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
