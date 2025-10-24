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
* Problem: 0572 - subtree_of_another_tree
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/subtree-of-another-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Notes:
        - find subtree
        - time: O(n*m)
        - space: O(n)
        """

        def is_same_tree(root, subRoot):
            if root == None and subRoot == None:  # both are none
                return True
            if (
                root == None or subRoot == None
            ):  # only one is none, since the last if condition was not met
                return False
            # at this point, neither nodes are none so time to check the value
            if root.val != subRoot.val:
                return False
            # at this point, no nodes are null and the values are the same, time to check children
            return is_same_tree(root.left, subRoot.left) and is_same_tree(
                root.right, subRoot.right
            )

        if root == None:
            return False
        if subRoot == None:
            return True
        if is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
