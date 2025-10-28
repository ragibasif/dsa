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
* Problem: 0021 - merge_two_sorted_lists
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/merge-two-sorted-lists/description/
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Notes:
        - time: O(n + m), check each element of both lists
        - space: O(1), no extra space created except for the dummy node and prev node
        - iterate and compare both lists using and conditional to avoid null pointer errors
        - after main while loop, check for the existence of both lists and add them to the end of the prev node
        """
        if not list1:
            return list2
        if not list2:
            return list1

        dummy = prev = ListNode(0, None)

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
            prev = prev.next
        if list2:
            prev.next = list2
            prev = prev.next

        return dummy.next
