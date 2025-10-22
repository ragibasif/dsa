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
* Problem: 0144 - binary_tree_preorder_traversal
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/binary-tree-preorder-traversal/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if not root:
            return res
        res.append(root.val)
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
        return res

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Notes:
        - preorder: parent -> left child -> right child
        - time: O(N), every node is visited
        - space: O(N), the recursive call stack can be O(N) in worst case since it can be the height of the tree which can be O(N/2) at most
        """
        if not root:
            return []

        res = []
        res = self.dfs(root, res)
        return res
