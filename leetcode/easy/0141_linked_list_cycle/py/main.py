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
* Problem: 0141 - linked_list_cycle
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/linked-list-cycle/description/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Notes:
        - two pointers, fast and slow
        - if there is a cycle then eventually the two pointers will meet and return true
        - if there is no cycle the fast pointer will reach null pointer
        - time: O(N)
        - space: O(1)
        """

        if not head:
            return False  # no cycle

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # found cycle

        return False  # no cycle
