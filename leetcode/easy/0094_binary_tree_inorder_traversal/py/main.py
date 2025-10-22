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
* Problem: 0094 - binary_tree_inorder_traversal
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Notes:
    - inorder traversal: left child -> parent -> right child
    - dfs (recursive):
        - time: O(n), every node will be visited
        - space: O(n), the recursive call stack can become as large as the maximum height of the tree which is O(n/2) --> O(n)
    """

    def dfs(self, root: Optional[TreeNode], res: List[int]) -> List[int]:
        if not root:
            return res
        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)
        return res

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        res = self.dfs(root, res)

        return res
