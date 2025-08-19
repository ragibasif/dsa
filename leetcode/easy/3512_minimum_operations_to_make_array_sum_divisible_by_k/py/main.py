"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3512 - minimum_operations_to_make_array_sum_divisible_by_k
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/minimum-operations-to-make-array-sum-divisible-by-k/description/
"""


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k
