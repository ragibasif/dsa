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
* Problem: 0102 - binary_tree_level_order_traversal
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Notes:
        - level order traversal, left to right
        - bfs
        - values only
        - time: O(n), each node is visited
        - space: O(n), queue can get as large as n/2 which is the max possible height of the tree
        """
        if not root:
            return []

        res = []
        queue = deque([root])
        while queue:
            q_len = len(queue)
            temp_arr = []
            for _ in range(q_len):
                node = queue.popleft()
                temp_arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(temp_arr)

        return res
