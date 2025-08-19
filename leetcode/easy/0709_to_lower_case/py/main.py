"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0709 - to_lower_case
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/to-lower-case/description/
"""


class Solution:
    def toLowerCase(self, s: str) -> str:
        res = ""
        for i in s:
            if ord(i) >= ord("A") and ord(i) <= ord("Z"):
                res += chr(ord(i) - ord("A") + ord("a"))
            else:
                res += i
        return res
