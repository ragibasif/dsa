"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1920 - build_array_from_permutation
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/build-array-from-permutation/description/
"""


# time: O(N)
# space: O(1) -> the output array is not counted in the space complexity
class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        and = []
        for i in range(len(nums)):
            and.append(nums[nums[i]])
        return and
