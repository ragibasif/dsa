"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3498 - reverse_degree_of_a_string
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/reverse-degree-of-a-string/description/
"""


class Solution:
    def reverseDegree(self, s: str) -> int:
        res_sum = 0
        for k, v in enumerate(s):
            res_sum += (ord("z") - ord(v) + 1) * (k + 1)
        return res_sum
