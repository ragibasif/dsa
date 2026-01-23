#include <iostream>
#include <cassert>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

template<typename A, typename B> ostream& operator<<(ostream &os, const pair<A, B> &p) { return os << '(' << p.first << ", " << p.second << ')'; }
template<typename T_container, typename T = typename enable_if<!is_same<T_container, string>::value, typename T_container::value_type>::type> ostream& operator<<(ostream &os, const T_container &v) { os << '{'; string sep; for (const T &x : v) os << sep << x, sep = ", "; return os << '}'; }
template<typename... T> void _dbg(T... args) { ((cerr << args << " "), ...); cerr << endl; }
#define dbg(...) cerr << "L" << __LINE__ << " [" << #__VA_ARGS__ << "]: ", _dbg(__VA_ARGS__)

class DynamicArray{
    public:
	DynamicArray(int size) : cnt(size) {
	    if (cnt < 0) { cnt = 1; }
	    cap = cnt << 1;
	    buf = new int[cap] {};
	    memset(buf,0,cap * sizeof *buf);
	}

	~DynamicArray() {
	    delete[] buf;
	    buf = nullptr;
	}

	int get(int idx) { // O(1)
	    assert(0 <= idx && idx < cnt);
	    return buf[idx];
	}

	void set(int idx, int val) { // O(1)
	    assert(0 <= idx && idx < cnt);
	    buf[idx] = val;
	}

	void print() { // O(N)
	    for (int i = 0; i < cnt; i++) {
		cout << buf[i] << " ";
	    }
	    cout << '\n';
	}

	int find(int val) { // O(N)
	    for (int i = 0; i < cnt; i++) {
		if (buf[i] == val) {
		    return i;
		}
	    }
	    return -1;
	}

	int get_front() {
	    return buf[0];
	}

	int get_back() {
	    return buf[cnt-1];
	}

	void push_back(int val) { // O(1) amortized
	    if (cnt +1 >= cap) {
		expand_cap();
	    }
	    buf[cnt++] = val;
	}

	int pop_back() {
	    if (cnt == 0) {
		return -1;
	    }
	    return buf[--cnt];
	}

    private:
	int *buf = nullptr;
	int cap = 0;
	int cnt = 0;

	void expand_cap() {
	    cap <<= 1;
	    int *nbuf = new int[cap] {};
	    memset(nbuf,0,cap * sizeof *nbuf);
	    for (int i = 0; i < cnt; i++) {
		nbuf[i] = buf[i];
	    }
	    swap(nbuf,buf);
	    delete[] nbuf;
	    nbuf = nullptr;
	}
};

class SinglyLinkedList {
    public:
	SinglyLinkedList() {
	    Node *node = new Node(42,nullptr);
	    Node *node1 = new Node(2,node);
	    Node *node2 = new Node(12,node1);
	    Node *node3 = new Node(43,node2);
	    Node *temp = node3;
	    while (temp) {
		temp->print();
		cout << " -> "; 
		temp = temp->next;
	    }
	    cout << '\n';
	}

	void print() {
	}
	~SinglyLinkedList() {}
    private:
	int len;
	struct Node *head;
	struct Node *tail;

	struct Node {
	    int data;
	    Node *next;

	    Node(int data, Node *next): data(data),next(next) {}
	    Node(int data): data(data),next(nullptr) {}
	    Node(): data(0),next(nullptr) {}

	    void print() {
		cout << data << " | " << next << " ";
	    }
	};
};


class Fiboncacci{
    public:
	Fiboncacci() {
	    memset(cache, -1, sizeof(cache)); 
	    cache[0] = 0;
	    cache[1] = 1;
	}
	/* Recursion: Top-Down */
	// this creates a binary tree of additions with only 0s and 1s as leaves
	int rec(int n) { // O(2ⁿ), exponential time
	    if (n <= 0) {
		return 0;
	    } else if(n==1) {
		return 1;
	    } else{
		return rec(n-1) + rec(n-2);
	    }
	}

	int memo(int n){
	    if (cache[n] != -1) {
		return cache[n];
	    } else{
		cache[n] = memo(n-1) + memo(n-2);
		return cache[n];
	    }
	}

	/* Iteration: Bottom-Up */
	int iter(int n) {
	    reset_cache();
	    cache[0] = 0;
	    cache[1] = 1;
	    for (int i = 2; i < n+1; i++) {
		cache[i] = cache[i-1] + cache[i-2];
	    }
	    return cache[n];
	}

	// uses the non-standard base case F₋₁ = 1 so that iter2(0) returns the correct value 0
	int iter2(int n) {
	    int prev = 1;
	    int curr = 0;
	    for (int i = 1; i < n+1; i++) {
		int next = curr + prev;
		prev = curr;
		curr = next;
	    }
	    return curr;
	}

    private:
	int cache[1<<19];
	void reset_cache() { memset(cache,-1,sizeof(cache)); }
};

int main() {

    Fiboncacci fib;
    dbg(fib.rec(23));
    dbg(fib.memo(23));
    dbg(fib.iter(23));
    dbg(fib.iter2(23));

    return 0;
}
