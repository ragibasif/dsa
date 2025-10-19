"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0033 - search_in_rotated_sorted_array
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Notes:
        - distinct
        - possibly left rotated
        - naive approach: linear search, O(N) time, O(1) space
        - optimized approach: binary search, O(log N) time, O(1) space
            - nums[right] < nums[left] and right > left == rotated portion
            - nums[right] > nums[left] and right > left == unrotated portion
        """

        def is_rotated(left, right) -> bool:
            return (nums[left] > nums[right]) and (left < right)

        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] > target:
                if not is_rotated(left, right):
                    right = middle - 1
                else:
                    if target > nums[left]:
                        left += 1
                    elif target < nums[left]:
                        left += 1
                    else:
                        return left
            elif nums[middle] < target:
                if not is_rotated(left, right):
                    left = middle + 1
                else:
                    if target > nums[right]:
                        right -= 1
                    elif target < nums[right]:
                        right -= 1
                    else:
                        return right
            else:
                return middle
        return -1
