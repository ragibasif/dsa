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
* Problem: 1448 - count_good_nodes_in_binary_tree
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    good_nodes = 0

    def goodNodes(self, root: TreeNode) -> int:
        """
        Notes:
        - maintain the path minimum for each subtree
        - maintain overall count of good nodes with global variable (optimize?)
        - dfs
        - time: O(n), all nodes are visited
        - space: O(n), recursive call stack can get as large as height of the tree
        """

        if not root:
            return 0

        def dfs(root, path_min):
            if not root:
                return
            if root.val >= path_min:
                self.good_nodes += 1
            path_min = max(path_min, root.val)
            if root.left:
                dfs(root.left, path_min)
            if root.right:
                dfs(root.right, path_min)

        path_min = root.val
        dfs(root, path_min)
        return self.good_nodes
