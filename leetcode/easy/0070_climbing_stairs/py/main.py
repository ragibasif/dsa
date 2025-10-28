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
* Problem: 0070 - climbing_stairs
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/climbing-stairs/description/
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Notes:
        - n steps to top
        - each time: 1 or 2
        - to get to n, we climbed one step from n-1 or two steps from n-2
        - examples:
            - n = 1 => 1
                -> 1
            - n = 2 => 2
                -> 1 1
                -> 2
            - n = 3 => 3
                -> 1 1 1
                -> 1 2
                -> 2 1
            - n = 4 => 5
                -> 1 1 1 1
                -> 1 1 2
                -> 1 2 1
                -> 2 1 1
                -> 2 2
        - fibonacci
        - get the previous 2 answers to get the current answer
        - dynamic programming
        - recursive
            - does not get accepted
            - time: O(N^2) due to redundant calculations
            - space: O(N^2), stack overflow
        - recursive memoization
            - gets accepted
            - time: O(N) more optimized than recursion due to memoization
            - space: O(N), hashmap of n items and recursive call stack

        - tabulation,iterative, bottom up
            - build an array with the number of ways that nth step can be
            - time: O(N)
            - space: O(N)
        - iterative, bottom up
            - the most optimized, constant space and linear time
            - time: O(N)
            - space: O(1)
        """

        if n < 1:
            return 1
        if n == 2:
            return 2

        # this does not get accepted due to pythons default maximum recursion limit of 1000 to help avoid stack overflow
        # ERROR: TLE
        def recursive(n):
            if n < 1:
                return 1
            if n == 1 or n == 2:
                return n
            return recursive(n - 1) + recursive(n - 2)

        def recursive_memoization(n, hash_map):
            if n < 1:
                return 1
            if n == 1 or n == 2:
                return n
            if n in hash_map:
                return hash_map[n]
            hash_map[n] = recursive_memoization(
                n - 1, hash_map
            ) + recursive_memoization(n - 2, hash_map)
            return hash_map[n]

        def iterative_arr(n):
            arr = [1] * (n + 1)
            arr[0] = 1
            arr[1] = 1
            for i in range(2, n + 1):
                arr[i] = arr[i - 1] + arr[i - 2]
            return arr[n]

        def iterative(n):
            first = 1
            second = 2
            if n <= 1:
                return first
            if n == 2:
                return second
            third = first + second
            for i in range(3, n + 1):
                third = first + second
                first = second
                second = third
            return third

        res = iterative_arr(n)
        return res
