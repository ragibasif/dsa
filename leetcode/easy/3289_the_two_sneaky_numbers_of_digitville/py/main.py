"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3289 - the_two_sneaky_numbers_of_digitville
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/description/
"""


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        hashset = set()
        for i in nums:
            if i in hashset:
                res.append(i)
                if len(res) == 2:
                    return res
            hashset.add(i)
        return res
