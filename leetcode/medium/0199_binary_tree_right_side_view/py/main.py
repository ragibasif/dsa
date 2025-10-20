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
* Problem: 0199 - binary_tree_right_side_view
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/binary-tree-right-side-view/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Notes:
        - return an array of the rightmost nodes at each level of the binary tree
        - the rightmost node does not necessarily have to be the right node, for example if a parent node has no node.right at all but has a node.left then that node.left is the rightmost node
        - why not dfs?
            - can't just go node.right all the way to last leaf node
        - bfs - level order traversal
            - create a queue and initialize with root node
            - iterate through the queue
                - pop the queue and append its children in order of left and right
                - last element in the queue is the rightmost
        - time: O(N), checking every node
        - space: O(N), queue can get as big as the max height of tree which is n/2
        """
        if not root:
            return []

        res = []
        queue = deque([root])  # FIFO
        while queue:
            q_size = len(queue)
            for _ in range(q_size):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            res.append(curr.val)

        # bfs algorithm
        return res
