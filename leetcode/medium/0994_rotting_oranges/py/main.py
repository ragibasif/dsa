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
* Problem: 0994 - rotting_oranges
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/rotting-oranges/description/
"""


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Notes:
        - bfs, time: O(V + E), space O(V + E)
        - 0 - empty (does not change)
        - 1 - fresh (can become rotten)
        - 2 - rotten
        - 4 directionally adjacent
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        - level order traversal
        - return min level until no fresh orange left
        - edge cases, no fresh, no rotten, no empty
        - add all rotten oranges to queue

        ex: 1
        [[2,1,1],
         [1,1,0],
         [0,1,1]]
                    ==> 4
        ex: 2
        [[2,1,1],
         [0,1,1],
         [1,0,1]]
                    ==> -1

        ex: 3
        [[0,2]]
                    ==> 0
        """

        def bounds_check(grid, row, col):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

        counter = 0

        def bfs(grid):
            t_counter = 0
            dx = [0, 1, 0, -1]
            dy = [1, 0, -1, 0]

            queue = deque()

            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 2:
                        queue.append((row, col))

            while queue:
                q_len = len(queue)
                flag = False
                for _ in range(q_len):
                    r, c = queue.popleft()
                    if grid[r][c] == 2:
                        for i in range(len(dx)):
                            new_r = r + dx[i]
                            new_c = c + dy[i]
                            if bounds_check(grid, new_r, new_c):
                                if grid[new_r][new_c] == 1:
                                    flag = True
                                    queue.append((new_r, new_c))
                                    grid[new_r][new_c] = 2
                if flag:
                    t_counter += 1
            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1:
                        return -1
            return t_counter

        counter = bfs(grid)

        return counter
