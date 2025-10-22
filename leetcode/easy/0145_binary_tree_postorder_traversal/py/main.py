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
* Problem: 0145 - binary_tree_postorder_traversal
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/binary-tree-postorder-traversal/description/
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
        if root.left:
            self.dfs(root.left, res)
        if root.right:
            self.dfs(root.right, res)
        res.append(root.val)
        return res

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Notes:
        - postorder: left child -> right child -> parent
        - dfs (recursive):
            - time: O(N), each node is visited
            - space: O(N), worst case, the recursive call stack can become as large as the height of the tree which can be maximum O(N/2) --> O(N)
        """
        if not root:
            return []

        res = []

        res = self.dfs(root, res)

        return res
