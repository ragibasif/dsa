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
* Problem: 0496 - next_greater_element_i
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/next-greater-element-i/description/
"""


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Notes:
        - monotonic stack
        - naive/brute force: nested loop to check all elements from the beginning, time: O(N^2)
        - optimised: start with the rightmost element and use a monotonic stack to maintain a decreasing sequence
        - Idea:
            - make a hash set of nums1
            - start at the rightmost of nums2
            - use nums1 as the results array
        """
        # time: O(N), space: O(N)
        hashmap = dict()
        for k, v in enumerate(nums1):
            hashmap[v] = k  # make the indices as values
        stack = []
        for idx in range(len(nums2) - 1, -1, -1):
            if not stack:
                stack.append(nums2[idx])
            if nums2[idx] in hashmap:
                if nums2[idx] < stack[-1]:
                    nums1[hashmap[nums2[idx]]] = stack[-1]
                else:
                    while stack and stack[-1] <= nums2[idx]:
                        stack.pop()
                    if not stack:
                        stack.append(nums2[idx])
                        nums1[hashmap[nums2[idx]]] = -1
                    else:
                        nums1[hashmap[nums2[idx]]] = stack[-1]

            stack.append(nums2[idx])

        return nums1
