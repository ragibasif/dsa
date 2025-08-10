"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 3541 - find_most_frequent_vowel_and_consonant
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/find-most-frequent-vowel-and-consonant/description/
"""


class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        consonants = defaultdict(int)
        for i in s:
            if i in vowels:
                vowels[i] += 1
            else:
                consonants[i] += 1
        max_v = 0
        max_c = 0
        for k, v in vowels.items():
            max_v = max(max_v, v)
        for k, v in consonants.items():
            max_c = max(max_c, v)
        return max_v + max_c
