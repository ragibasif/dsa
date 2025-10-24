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
* Problem: 0680 - valid_palindrome_ii
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/valid-palindrome-ii/description/
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Notes:
        - two pointers
        - at most one char can change (only one pair not matching)
        - check palindrome as normal, when chars not same, check palindromicity for only shifting up the left pointer and only shifting down the right pointer
        - Time: O(N)
        - Space: O(1)
        """
        if len(s) <= 1:
            return True
        left = 0
        right = len(s) - 1
        diff = 0

        def is_palindrome(s, l, r):
            while l <= r:
                if s[l] == s[r]:
                    l += 1
                    r -= 1
                else:
                    return False
            return True

        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return is_palindrome(s, left + 1, right) or is_palindrome(
                    s, left, right - 1
                )
        return True
