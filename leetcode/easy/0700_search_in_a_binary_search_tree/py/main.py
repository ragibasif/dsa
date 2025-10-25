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
* Problem: 0700 - search_in_a_binary_search_tree
* Platform: leetcode
* Difficulty: easy
* URL: https://leetcode.com/problems/search-in-a-binary-search-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Notes:
        - bfs
        - time: O(n), each node is visited (worst case)
        - space: O(n), queue can get as large as n/2 which is the maximum height of a binary search tree (worst case)
        """
        if not root:
            return None

        queue = deque([root])
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.popleft()
                if node.val == val:
                    return node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return None
