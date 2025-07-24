"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0226 - invert_binary_tree
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/invert-binary-tree/
"""

# recursive
# time: O(N)
# space: O(N) recursive stack space, very inefficient


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        if root.right or root.left:
            root.right, root.left = root.left, root.right
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root
