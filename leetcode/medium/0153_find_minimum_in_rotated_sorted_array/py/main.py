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
* Problem: 0153 - find_minimum_in_rotated_sorted_array
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
"""


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Notes:
        - binary search (sorted array, O(log n) time)
        - find minimum
        - unique elements
        - n >= 1 (guaranteed an answer)
        - if n-1 == max, then 0 == min
        - if n-k == max, then n-k+1 == min, given k > 1
        - time: O(log n)
        - space: O(1)
        """

        left = 0
        right = len(nums) - 1

        def is_rotated(left, right):
            return nums[left] > nums[right]

        while left <= right:
            middle = (right + left) // 2

            if is_rotated(left, right):
                if nums[middle] > nums[right]:
                    left = middle + 1
                else:
                    right = middle
            else:
                return nums[left]
