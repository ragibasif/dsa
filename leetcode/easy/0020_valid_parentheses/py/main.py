"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0020 - valid_parentheses
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/valid-parentheses/description/
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == "(" or i == "[" or i == "{":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == "(" and i == ")":
                    stack.pop()
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                elif stack[-1] == "{" and i == "}":
                    stack.pop()
                else:
                    return False

        return len(stack) == 0
