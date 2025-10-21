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
        # Time: O(N)
        # Space: O(1)
        stack = []

        def peek():
            return stack[-1]

        def empty():
            return len(stack) == 0

        def push(n):
            stack.append(n)

        def pop():
            return stack.pop()

        paren_map = {"(": ")", "[": "]", "{": "}"}
        for i in s:
            if i in paren_map:
                push(i)
            else:
                if not empty() and paren_map[peek()] == i:
                    pop()
                else:
                    return False

        return empty()
