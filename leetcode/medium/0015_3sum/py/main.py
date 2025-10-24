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
* Problem: 0015 - 3sum
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/3sum/description/
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Notes:
        - not sorted
        - naive: 3 nested loops
        - optimized: two pointers
        - idea 1: sort input
        - time: O(N^2)
        - space: O(1) (O(N) for python since it uses timsort which uses O(N) space)
            - https://stackoverflow.com/questions/48759175/what-is-the-space-complexity-of-the-python-sort
            - https://en.wikipedia.org/wiki/Timsort
        """

        nums.sort()
        res = []
        for first in range(len(nums) - 2):
            if nums[first] > 0:  # no point in continuing past 0 since its sorted
                break
            if (
                first > 0 and nums[first] == nums[first - 1]
            ):  # duplicate elements get skipped
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                tot = nums[first] + nums[second] + nums[third]
                if tot == 0:
                    res.append([nums[first], nums[second], nums[third]])
                    second += 1
                    while (
                        nums[second] == nums[second - 1] and second < third
                    ):  # duplicate elements get skipped
                        second += 1
                elif tot > 0:
                    third -= 1
                else:  # tot < 0
                    second += 1

        return res
