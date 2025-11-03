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
* Problem: 0695 - max_area_of_island
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/max-area-of-island/description/
"""


class Solution:
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    dirs = len(dx)

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Notes:
        - iterate through the grid and if a 1 is found, count all connected 1 and mark them as you go
        - only dx,dy
        - keep track of max
        - 0 == water
        - 1 == land
        - out of bounds == water
        - -1 == mark
        - dfs
        - bfs
        - time: O(mn)
        - space: O(mn)
        """

        def check_bounds(grid, row, col):
            return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0])

        def dfs(grid, row, col):
            if grid[row][col] == -1 or grid[row][col] == 0:
                return 0
            counter = 1
            grid[row][col] = -1
            for i in range(self.dirs):
                new_row = row + self.dx[i]
                new_col = col + self.dy[i]
                if check_bounds(grid, new_row, new_col):
                    counter += dfs(grid, new_row, new_col)
            return counter

        def bfs(grid, row, col):
            queue = deque([(row, col)])
            counter = 1
            grid[row][col] = -1
            while queue:
                curr_row, curr_col = queue.popleft()
                for i in range(self.dirs):
                    new_row = curr_row + self.dx[i]
                    new_col = curr_col + self.dy[i]
                    if check_bounds(grid, new_row, new_col):
                        if grid[new_row][new_col] == 1:
                            counter += 1
                            grid[new_row][new_col] = -1
                            queue.append((new_row, new_col))
            return counter

        max_area = 0
        len_row = len(grid)
        len_col = len(grid[0])
        for row in range(len_row):
            for col in range(len_col):
                if grid[row][col] == 1:
                    # max_area = max(max_area, dfs(grid,row,col))
                    max_area = max(max_area, bfs(grid, row, col))

        return max_area
