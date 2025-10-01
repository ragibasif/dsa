"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0383 - ransom_note
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/ransom-note/description/
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # time: O(N)
        # space: O(1), even though we use a hashmap, the constraint is lowercase English letters, so the max the hashmap will take up is O(26) which is O(1)
        char_hashmap = defaultdict(int)
        for m in magazine:
            char_hashmap[m] += 1
        for r in ransomNote:
            if r not in char_hashmap or char_hashmap[r] == 0:
                return False
            char_hashmap[r] -= 1
        return True
