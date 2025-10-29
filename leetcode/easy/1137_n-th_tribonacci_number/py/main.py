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
* Problem: 1137 - n-th_tribonacci_number
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/n-th-tribonacci-number/
"""


class Solution:
    def tribonacci(self, n: int) -> int:
        """
        Notes:
        - similar to fibonacci except with extra item
        - t0 = 0
        - t1 = 1
        - t2 = 1
        """
        if n <= 0:
            return 0
        if n == 1 or n == 2:
            return 1

        rec_res = 0
        rec_res_memo = 0
        iter_res = 0
        iter_res_final = 0

        # TLE, time: O(n^2), top down
        def rec(n):
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return 1
            return rec(n - 1) + rec(n - 2) + rec(n - 3)

        # rec_res = rec(n)

        # AC, recursive with memoization, time: O(n), space: O(n) (hashmap and recursive call stack), top down with recursion
        def rec_memo(n, memo):
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n not in memo:
                memo[n] = (
                    rec_memo(n - 1, memo)
                    + rec_memo(n - 2, memo)
                    + rec_memo(n - 3, memo)
                )
            return memo[n]

        # memo = { 0: 0, 1: 1, 2: 1 }
        # rec_res_memo = rec_memo(n,memo)

        # iteraive, bottom up with dp array, O(n) time and space
        def iterative(n):
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return 1
            # presumably atp, n >= 3
            dp = [0] * (n + 1)  # index ranges from 0 to n
            dp[0] = 0
            dp[1] = 1
            dp[2] = 1
            for i in range(3, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
            return dp[n]

        # iter_res = iterative(n)
        # bottom up iterative, most optimized, time: O(n), space: O(1)
        def iter_final(n):
            if n <= 0:
                return 0
            if n == 1 or n == 2:
                return 1
            # presumably atp, n >= 3
            one = 0
            two = 1
            three = 1
            for i in range(3, n + 1):
                four = one + two + three
                one = two
                two = three
                three = four
            return three

        iter_res_final = iter_final(n)

        return iter_res_final
