"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1678 - goal_parser_interpretation
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/goal-parser-interpretation/
"""


class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                res += "G"
                i += 1
            elif command[i] == "(" and command[i + 1] == ")":
                res += "o"
                i += 2
            else:
                res += "al"
                i += 4
        return res
