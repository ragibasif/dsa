"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0278 - first_bad_version
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/first-bad-version/description/
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """
        Notes:
        - left biased binary search
        - assuming the answer is guaranteed
        - time: O(log N)
        - space: O(1)
        """
        if n == 1:
            return 1
        left = 1
        right = n
        res = left
        while left <= right:
            middle = (right + left) // 2
            if not isBadVersion(middle):
                left = middle + 1
            else:
                res = middle
                if isBadVersion(middle - 1):
                    right = middle - 1
                else:
                    break
        return res
