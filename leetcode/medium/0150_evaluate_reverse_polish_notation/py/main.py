"""
* File: main.py
* Author: Ragib Asif
* Email: ragibasif@tuta.io
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0150 - evaluate_reverse_polish_notation
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
"""


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Notes:
        - stack problem
        - floor division
        - valid input
        - Time: O(N), every element is checked
        - Space: O(N), worst case, nearly all elements might be in the stack

        - learned: storing functions in dictionaries, very convenient and fun
        - https://stackoverflow.com/questions/37283786/floor-division-with-negative-number
            - better understood how floor division works and how truncate to zero works in python
            - '//' will only floor the result: a // b
            -  to truncate towards zero: int(a / b)
        """

        def add(a, b):
            return a + b

        def sub(a, b):
            return a - b

        def mul(a, b):
            return a * b

        def div(a, b):
            return int(a / b)

        op_map = {"+": add, "-": sub, "*": mul, "/": div}
        stack = []

        for tok in tokens:
            if tok not in op_map:
                if tok[0] == "-":
                    stack.append(-1 * int(tok[1:]))
                else:
                    stack.append(int(tok))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(op_map[tok](op1, op2))

        return stack.pop()
