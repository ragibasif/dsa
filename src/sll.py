#!/usr/bin/env python3

from utils import trace, benchmark, report, inspect


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"        


@benchmark
def build_sll(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

@benchmark
def debug_sll(head):
    res = []
    curr = head
    seen = set()
    bound = 25
    
    while curr:
        node_id = id(curr)
        if node_id in seen:
            res.append(f"Cycle({curr.val})")
            break
        
        seen.add(node_id)
        res.append(str(curr.val))
        curr = curr.next
        
        if len(res) >= bound:
            res.append("...")
            break
    
    if not curr and len(res) < bound + 1:
        res.append("None")
        
    res = " -> ".join(res)
    print(res)

def main():
    arr = [5, 10, 9, 6, 10, 4, 8, 1, 9, 4]
    node = build_sll(arr)
    debug_sll(node)
    node.next.next.next.next = node
    debug_sll(node)

if __name__ == "__main__":
    main()
