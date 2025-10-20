"""
* File: main.py
* Author: Ragib Asif
* GitHub: https://github.com/ragibasif
* LinkedIn: https://www.linkedin.com/in/ragibasif/
* SPDX-License-Identifier: MIT
* Copyright (c) 2025 Ragib Asif
* Version 1.0.0
*
* Problem: 0110 - balanced_binary_tree
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/balanced-binary-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Notes:
        - height balanced - no node's left subtree and right subtree have a height difference greater than one
        - all subtrees need to be balanced, if one subtree is imbalanced then the entire tree is imbalanced
        - check at each node that it is a valid subtree
        - dfs/bfs
        - get the height of each subtree
        - height of a tree is equal to the depth of its deepest subtree
        - height = 1 + max(left_height, right_height)

        method 1: dfs
        time: O(n), every node is visited
        space: O(n), recursive call stack since max possible height of binary tree is n
        """

        def get_height(node) -> int:
            if not node:
                return 0
            l = get_height(node.left)
            r = get_height(node.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return 1 + max(l, r)

        if not root:
            return True
        left = get_height(root.left)
        right = get_height(root.right)
        if left == -1 or right == -1:
            return False
        return abs(right - left) <= 1
