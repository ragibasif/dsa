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
* Problem: 0200 - number_of_islands
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/number-of-islands/description/
"""


class Solution:

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dirs = 4

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Notes:
        1 = land
        0 = water
        x = mark
        can only move horizontally and vertically
        dx = [0,1,0,-1]
        dy = [1,0,-1,0]
        dfs
        out of bounds == water
        time: O(mn)
        space: O(mn)
        bfs: time O(mn), space O(mn)
        """

        def check_bounds(grid, row, col):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

        def dfs(grid, row, col):
            if grid[row][col] == "x":
                return
            if grid[row][col] == "0":
                return

            if grid[row][col] == "1":
                grid[row][col] = "x"

            for i in range(self.dirs):
                new_r = row + self.dx[i]
                new_c = col + self.dy[i]
                if check_bounds(grid, new_r, new_c):
                    dfs(grid, new_r, new_c)
            return

        def bfs(grid, row, col):
            queue = deque([(row, col)])
            while queue:
                r, c = queue.popleft()
                for i in range(self.dirs):
                    new_r = r + self.dx[i]
                    new_c = c + self.dy[i]
                    if check_bounds(grid, new_r, new_c):
                        if grid[new_r][new_c] == "1":
                            grid[new_r][new_c] = "x"
                            queue.append((new_r, new_c))

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    # dfs(grid,row,col)
                    bfs(grid, row, col)
        return count
