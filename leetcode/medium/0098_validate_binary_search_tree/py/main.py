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
* Problem: 0098 - validate_binary_search_tree
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/validate-binary-search-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Notes:
        - dfs
        - use inorder traversal to build an array then check array is sorted
        - time: O(n); all nodes are visited
        - space: O(n); recursive call stack can get as large as the height of the tree
        """

        arr = []

        def dfs(root, arr):
            if not root:
                return []
            if root.left:
                dfs(root.left, arr)
            arr.append(root.val)
            if root.right:
                dfs(root.right, arr)
            return arr

        def check_sorted(arr):
            for i in range(len(arr) - 1):
                if arr[i] >= arr[i + 1]:
                    return False
            return True

        arr = dfs(root, arr)

        return check_sorted(arr)
