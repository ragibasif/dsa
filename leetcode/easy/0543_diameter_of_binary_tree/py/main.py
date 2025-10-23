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
* Problem: 0543 - diameter_of_binary_tree
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/diameter-of-binary-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    max_path_subtree = 0

    def dfs(self, root):
        if not root:
            return 0
        max_path_left = 0
        max_path_right = 0
        if root.left:
            max_path_left = self.dfs(root.left) + 1
        if root.right:
            max_path_right = self.dfs(root.right) + 1
        self.max_path_subtree = max(
            self.max_path_subtree, max_path_left + max_path_right
        )
        return max(max_path_left, max_path_right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Notes:
        - dfs
        - count the edges
        - keep track of max paths of subtrees
        - time: O(N), all nodes are visited
        - space: O(N), recursive call stack can be as large as n/2

        - a = parent -> left child = 1
        - b = parent -> right child = 1
        - c = left child -> right child  = a + b = 2

        - challenges:
            - did not read and understand the problem at first and spent a long time trying to solve a different much more difficult problem
            - had errors with maintaining the max of subtrees due to negligence with global variables
        """
        if not root:
            return 0

        r_left = 0
        r_right = 0
        if root.left:
            r_left = self.dfs(root.left) + 1
        if root.right:
            r_right = self.dfs(root.right) + 1
        self.max_path_subtree = max(self.max_path_subtree, r_right + r_left)

        return self.max_path_subtree
