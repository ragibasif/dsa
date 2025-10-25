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
* Problem: 0235 - lowest_common_ancestor_of_a_binary_search_tree
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Notes:
        - if p or q == root -> return root
        - if (p > root and q < root) or (p < root and q > root) -> return root
        - dfs
            - time: O(n), worst case all nodes are visited
            - space: O(n), worst case the call stack is as large as the height of the tree which can be n/2 at most
        """

        if (
            (p.val == root.val or q.val == root.val)
            or (p.val > root.val and q.val < root.val)
            or (p.val < root.val and q.val > root.val)
        ):
            return root
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return self.lowestCommonAncestor(root.right, p, q)
