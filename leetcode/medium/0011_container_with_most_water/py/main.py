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
* Problem: 0011 - container_with_most_water
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/container-with-most-water/description/
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Notes:
        - two pointers
        - keep track of max area
        - area calculation:
            - a = right_ptr - left_ptr
            - b = min(height[left_ptr], height[right_ptr])
            - area = a * b
            - max_area = max(max_area, area)
        time: O(N)
        space: O(1)
        """
        max_area = -math.inf
        left = 0
        right = len(height) - 1
        while left < right:
            ptr_dist = right - left
            min_height = min(height[left], height[right])
            curr_area = ptr_dist * min_height
            max_area = max(max_area, curr_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area
