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
* Problem: 0746 - min_cost_climbing_stairs
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/min-cost-climbing-stairs/
"""


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        Notes:
        - can start at index 0 or 1
        - landing on an index means you need to pay that cost
        - similar to fib where you can go 1 or 2 steps
        - dp
        - always keep track and consider the minimum
        - we want the minimum from both paths and minimum the minimum of both paths
        - min((path 1), (path 2))
        - recurrence:
        """

        # TLE, top-down,time: O(n^2)
        def my_recursive(cost, i):
            if n < 0:
                return 0
            # starting positions cost are just what they are
            if i == 0 or i == 1:
                return cost[i]
            res = cost[i] + min(my_recursive(cost, i - 1), my_recursive(cost, i - 2))
            return res

        # my_res_rec = min(my_recursive(cost,len(cost)-1),my_recursive(cost,len(cost)-2))

        # accepted after changing dp array default nums to -1 from 0
        # time: O(n), space: O(n)
        def my_recursive_memo(cost, i, dp):
            if i < 0:
                return 0
            # starting positions cost are just what they are
            if i == 0 or i == 1:
                return cost[i]
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(
                my_recursive_memo(cost, i - 1, dp), my_recursive_memo(cost, i - 2, dp)
            )
            return dp[i]

        # len_c = len(cost)
        # dp = [-1] * len_c
        # my_res_rec_memo = min(my_recursive_memo(cost,len_c-1,dp),my_recursive_memo(cost,len_c-2,dp))

        # bottom up iterative, time: O(n), space: O(n)
        def bot_up_iter(cost):
            len_c = len(cost)
            dp = [-1] * len_c
            # given constraint, len is minimum 2
            dp[0] = cost[0]
            dp[1] = cost[1]
            for i in range(2, len_c):
                dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            res = min(dp[len_c - 1], dp[len_c - 2])
            return res

        # my_res_bot_up_iter = bot_up_iter(cost)

        # final optimization, time: O(n), space: O(1)
        def final_bot_up_iter(cost):
            len_c = len(cost)
            # given constraint, len is minimum 2
            first = cost[0]
            second = cost[1]
            for i in range(2, len_c):
                curr = cost[i] + min(first, second)
                first = second
                second = curr
            res = min(first, second)
            return res

        my_final_res_bot_up_iter = final_bot_up_iter(cost)

        return my_final_res_bot_up_iter
