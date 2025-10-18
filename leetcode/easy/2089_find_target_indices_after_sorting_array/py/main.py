"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 2089 - find_target_indices_after_sorting_array
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/find-target-indices-after-sorting-array/description/
"""


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """
        Notes:
        - step 0: edge cases, does target exist in array, empty array, etc.
        - step 1: sort the array
        - step 2: find first and last occurrence
        - step 3: add all occurrences to result array
        - time: O(N log N)
        - space: O(1)
        """

        def target_exists(item):
            for elem in nums:
                if elem == item:
                    return True
            return False

        if not target_exists(target):
            return []

        left = 0
        right = len(nums) - 1
        nums.sort()  # O(n log n)
        first = last = -1
        # left biased
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:  # nums[middle] == target
                first = middle
                if (middle - 1) >= 0:
                    right = middle - 1
                else:
                    break
        left = 0
        right = len(nums) - 1
        # right biased
        while left <= right:
            middle = (right + left) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:  # nums[middle] == target
                last = middle
                if (middle + 1) < len(nums):
                    left = middle + 1
                else:
                    break
        if last == -1:
            last = first
        result = []
        for idx in range(first, last + 1):
            result.append(idx)
        return result
