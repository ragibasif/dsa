"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 1684 - count_the_number_of_consistent_strings
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/count-the-number-of-consistent-strings/description/
"""


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        new_allowed_set = set(allowed)
        counter = 0
        for i in words:
            temp_word_set = set(i)
            flag = True
            for j in temp_word_set:
                if j not in new_allowed_set:
                    flag = False
            if flag:
                counter += 1
        return counter
