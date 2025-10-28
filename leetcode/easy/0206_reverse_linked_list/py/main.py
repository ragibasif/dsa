"""
* File: main.py
* Author: Ragib Asif
* Email: ragibasif@tuta.io
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0206 - reverse_linked_list
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/reverse-linked-list/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Notes:
        - iterative
            - time: O(N), all nodes are visited
            - space: O(1)
        - recursive
            - refactored version of the iterative, use recursion to handle the looping and the base case should be the while condition
            - time: O(N), all nodes are visited
            - space: O(N), the recursive call stack will take a lot of space
        """

        if not head:
            return head

        def iterative(head):
            prev = None
            curr = head
            while curr:
                n_curr = curr.next
                curr.next = prev
                prev = curr
                curr = n_curr
            return prev

        def recursive(curr, prev):
            if not curr:
                return prev
            n_curr = curr.next
            curr.next = prev
            prev = curr
            curr = n_curr
            return recursive(curr, prev)

        # iter_res = iterative(head)
        recur_res = recursive(head, None)

        return recur_res
