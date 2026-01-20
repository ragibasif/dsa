#include <iostream>
#include <cassert>
#include <string>
#include <utility>
#include <vector>
#include <unordered_map>
#include <unordered_set>

using namespace std;

#define dbg(x) cerr << "Line(" << __LINE__ << ") -> " << #x << " = " << (x) << endl;

class DynamicArray{
    public:
	DynamicArray(int sz) : sz(sz) {
	    if (sz < 0) { sz = 1; }
	    cap = sz << 1;
	    buf = new int[cap] {};
	    memset(buf,0,cap * sizeof *buf);
	}

	~DynamicArray() {
	    delete[] buf;
	    buf = nullptr;
	}

	int get(int idx) { // O(1)
	    assert(0 <= idx && idx < sz);
	    return buf[idx];
	}

	void set(int idx, int val) { // O(1)
	    assert(0 <= idx && idx < sz);
	    buf[idx] = val;
	}

	void print() { // O(N)
	    for (int i = 0; i < sz; i++) {
		cout << buf[i] << " ";
	    }
	    cout << '\n';
	}

	int find(int val) { // O(N)
	    for (int i = 0; i < sz; i++) {
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
	    return buf[sz-1];
	}

	void push_back(int val) { // O(1) amortized
	    if (sz +1 >= cap) {
		expand_cap();
	    }
	    buf[sz++] = val;
	}

	int pop_back() {
	    if (sz == 0) {
		return -1;
	    }
	    return buf[--sz];
	}

    private:
	int *buf = nullptr;
	int cap = 0;
	int sz = 0;

	void expand_cap() {
	    cap <<= 1;
	    int *nbuf = new int[cap] {};
	    memset(nbuf,0,cap * sizeof *nbuf);
	    for (int i = 0; i < sz; i++) {
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

int main() {
    
    SinglyLinkedList sll;

    return 0;
}
