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
* Problem: 0213 - house_robber_ii
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/house-robber-ii/description/
"""


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        Notes:
        - similar to House Robber 1 but with an extra edge case
        - check that if last element is used then first element isn't and vice versa
        - dp
        - recurrence relation:
            - path1: start with index 0 and throw out the last index
            - path2: throw out index 0 and start with index 1 to last
        """
        res = 0

        # TLE, recursive top down, time: O(n^2)
        def rec(nums, n):
            if n < 0:
                return 0
            path1 = nums[n] + max(rec(nums, n - 2), rec(nums, n - 3))
            path2 = rec(nums, n - 1)
            return max(path1, path2)

        # res = max(rec(nums[0:1] + nums[1:len(nums)-1],len(nums[0:1] + nums[1:len(nums)-1])-1),rec(nums[1:],len(nums[1:])-1))

        # AC, recursive top down with memoization, time: O(n), space: O(n) hashmap and recursive call stack
        def rec_memo(nums, n, memo):
            if n < 0:
                return 0
            path1 = nums[n]
            if (n - 2) not in memo:
                memo[n - 2] = rec_memo(nums, n - 2, memo)
            if (n - 3) not in memo:
                memo[n - 3] = rec_memo(nums, n - 3, memo)

            path1 = nums[n] + max(memo[n - 2], memo[n - 3])
            path2 = rec_memo(nums, n - 1, memo)
            return max(path1, path2)

        # res = max(rec_memo(nums[0:1] + nums[1:len(nums)-1],len(nums[0:1] + nums[1:len(nums)-1])-1,{}),rec_memo(nums[1:],len(nums[1:])-1,{}))

        # iterative bottom up dp, time: O(n), space: O(n) 2 dp arrays
        def iter_dp(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])
            # safe to assume len(nums) > 2
            dp1 = [-1] * len(nums)
            dp1[0] = nums[0]
            dp1[1] = nums[1]
            dp2 = [-1] * len(nums)
            dp2[0] = nums[0]
            dp2[1] = nums[1]
            max1 = 0
            for i in range(0, len(nums) - 1):
                dp1[i] = nums[i]
                if i - 2 >= 0:
                    if i - 3 >= 0:
                        dp1[i] += max(dp1[i - 2], dp1[i - 3])
                    else:
                        dp1[i] += dp1[i - 2]
                max1 = max(max1, dp1[i])
            max2 = 0
            for i in range(1, len(nums)):
                dp2[i] = nums[i]
                if i - 2 >= 1:
                    if i - 3 >= 1:
                        dp2[i] += max(dp2[i - 2], dp2[i - 3])
                    else:
                        dp2[i] += dp2[i - 2]
                max2 = max(max2, dp2[i])
            return max(max1, max2)

        # iter + N variables, time: O(n) 2 for loops, space: O(1)
        def iter_opt(nums):
            if len(nums) == 1:
                return nums[0]
            if len(nums) == 2:
                return max(nums[0], nums[1])

            dp1_sub_3 = 0
            dp1_sub_2 = 0
            dp1_sub_1 = 0
            max1 = 0
            for i in range(0, len(nums) - 1):
                dp1_t = nums[i]
                if i - 2 >= 0:
                    if i - 3 >= 0:
                        dp1_t += max(dp1_sub_3, dp1_sub_2)
                    else:
                        dp1_t += dp1_sub_2
                dp1_sub_3 = dp1_sub_2
                dp1_sub_2 = dp1_sub_1
                dp1_sub_1 = dp1_t
                max1 = max(max1, dp1_t)

            dp2_sub_3 = 0
            dp2_sub_2 = 0
            dp2_sub_1 = 0
            max2 = 0
            for i in range(1, len(nums)):
                dp2_t = nums[i]
                if i - 2 >= 1:
                    if i - 3 >= 1:
                        dp2_t += max(dp2_sub_3, dp2_sub_2)
                    else:
                        dp2_t += dp2_sub_2
                dp2_sub_3 = dp2_sub_2
                dp2_sub_2 = dp2_sub_1
                dp2_sub_1 = dp2_t
                max2 = max(max2, dp2_t)
            return max(max1, max2)

        res = iter_opt(nums)

        return res
