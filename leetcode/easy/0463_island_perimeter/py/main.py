"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0463 - island_perimeter
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/island-perimeter/description/
"""


# dfs
# time: O(V+E)
# space: O(V+E), recursive calls
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # the parts touching water count as a perimeter
        # dfs
        if not grid or not grid[0]:
            return 0
        perimeter = 0
        row_len = len(grid)
        col_len = len(grid[0])
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == 1:
                    perimeter += self.dfs(grid, row, col)
        return perimeter

    def dfs(self, grid, r, c):
        if grid[r][c] == -1:
            return 0
        if grid[r][c] == 1:
            grid[r][c] = -1
        if grid[r][c] == 0:
            return 1
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        counter = 0
        for d in range(len(dirs)):
            new_r = r + dirs[d][0]
            new_c = c + dirs[d][1]
            if self.bounds_check(grid, new_r, new_c):
                counter += self.dfs(grid, new_r, new_c)
            else:
                counter += 1
        return counter

    def bounds_check(self, grid, r, c):
        return 0 <= r < len(grid) and 0 <= c < len(grid[0])
