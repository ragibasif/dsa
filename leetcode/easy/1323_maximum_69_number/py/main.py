"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1323 - maximum_69_number
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/maximum-69-number/description/
"""


class Solution:
    def maximum69Number(self, num: int) -> int:
        to_str = str(num)
        res = ""
        for i in range(len(to_str)):
            if to_str[i] == "6":
                res += "9"
                res += to_str[i + 1 :]
                return int(res)
            res += to_str[i]
        return int(res)
