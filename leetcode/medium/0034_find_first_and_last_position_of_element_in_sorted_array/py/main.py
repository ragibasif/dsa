"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0034 - find_first_and_last_position_of_element_in_sorted_array
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        Notes:
        - always sorted in non-decreasing
        - left biased binary search for the first occurrence
        - right biased binary search for the last occurrence
        - empty array -> [-1,-1]
        - not found -> [-1,-1]
        - time: O(log N)
        - space: O(1)
        """

        first = last = -1

        error_arr = [first, last]
        if len(nums) == 0:
            return error_arr

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right + left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                if (middle - 1) >= 0:
                    if nums[middle - 1] != target:
                        first = middle
                        break
                    else:
                        right = middle - 1
                else:
                    first = middle
                    break

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
            else:
                if (middle + 1) < len(nums):
                    if nums[middle + 1] != target:
                        last = middle
                        break
                    else:
                        left = middle + 1
                else:
                    last = middle
                    break

        if last == -1:
            last = first
        return [first, last]
