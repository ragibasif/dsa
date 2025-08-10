"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0128 - longest_consecutive_sequence
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/longest-consecutive-sequence/description/
"""


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # add to hashset
        # start at the largest number in the sequence and then countdown
        hashset = set(nums)
        counter = 0
        for i in hashset:
            j = i
            temp = 0
            if j + 1 not in hashset:
                while j - 1 in hashset:
                    temp += 1
                    j -= 1
            counter = max(counter, temp)
        if len(nums) > 0:
            counter += 1
        return counter
