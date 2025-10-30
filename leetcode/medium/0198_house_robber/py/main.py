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
* Problem: 0198 - house_robber
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/house-robber/description/
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Notes:
        - 2 paths
            - even indexes sum
            - odd indexes sum
        - first and last indices are not considered adjacent if there are elements between them (they don't wrap)
        - recursive relation -> recursive (top-down) -> recursive + memo (top-down) -> iterative + memo (bottom-up) -> iterative + N variables (bottom-up)
        - max(n + n-2, n - 1)
        """

        # TLE (50/70 testcases passed), time: O(n ^ 2)
        def rec(nums, n):
            if n < 0:
                return 0
            path1 = rec(nums, n - 1)
            path2 = rec(nums, n - 2) + nums[n]
            return max(path1, path2)

        # accepted, time: O(n), space: O(n) hashmap + recursive call stack
        def rec_memo(nums, n, memo):
            if n < 0:
                return 0
            if (n - 1) not in memo:
                memo[n - 1] = rec_memo(nums, n - 1, memo)
            if (n - 2) not in memo:
                memo[n - 2] = rec_memo(nums, n - 2, memo)
            path1 = memo[n - 1]
            path2 = memo[n - 2] + nums[n]
            return max(path1, path2)

        # time: O(n), space: O(n)
        def iter_memo(nums):
            if len(nums) < 1:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [-1] * len(nums)  # elements in nums are >= 0
            # fair to assume the len is greater than or equal to 2
            dp[0] = nums[0]
            dp[1] = nums[1]
            for i in range(2, len(nums)):
                dp[i] = nums[i]
                if ((i - 2) >= 0) and ((i - 2 - 1) >= 0):
                    dp[i] += max(dp[i - 2], dp[i - 2 - 1])
                else:
                    dp[i] += dp[i - 2]
            last = len(dp) - 1
            return max(dp[last], dp[last - 1])

        # time: O(n), space: O(1)
        def iter_optimized(nums):
            if len(nums) < 1:
                return 0
            if len(nums) == 1:
                return nums[0]
            i_sub_3 = -1
            i_sub_2 = nums[0]
            i_sub_1 = nums[1]
            for i in range(2, len(nums)):
                curr = nums[i]
                curr += max(i_sub_2, i_sub_3)
                i_sub_3 = i_sub_2
                i_sub_2 = i_sub_1
                i_sub_1 = curr
            return max(i_sub_1, i_sub_2)

        res = iter_optimized(nums)

        return res
