"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0058 - length_of_last_word
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/length-of-last-word/description/
"""


# time: O(N)
# space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        counter = 0
        i = len(s) - 1
        while s[i] == " " and i >= 0:
            i -= 1
        j = i
        while s[j] != " " and j >= 0:
            counter += 1
            j -= 1
        return counter


# time: O(N)
# space: O(1)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # start from the end of input string
        # iterate until no whitespace
        # count chars until whitespace
        counter = 0
        flag = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and not flag:
                continue
            elif s[i] == " " and flag:
                break
            else:
                flag = True
                counter += 1
        return counter
