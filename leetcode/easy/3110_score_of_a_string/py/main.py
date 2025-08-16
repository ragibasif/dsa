"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3110 - score_of_a_string
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/score-of-a-string/description/
"""

# time: O(N)
# space: O(1)


class Solution:
    def scoreOfString(self, s: str) -> int:
        # get ascii value: ord(x)
        # sum the ascii values
        score = 0
        for i in range(len(s) - 1):
            score += abs(ord(s[i]) - ord(s[i + 1]))
        return score
