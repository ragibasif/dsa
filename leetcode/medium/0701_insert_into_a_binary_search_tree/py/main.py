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
* Problem: 0701 - insert_into_a_binary_search_tree
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/insert-into-a-binary-search-tree/description/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        """
        Notes:
        - decide on path based on root val
        - dfs (recursive)
            - time: O(n), all nodes are visited
            - space: O(n), recursive call stack can get as large as n/2 which is the max height of the tree
        - bfs (iterative)
            - time: O(n), all nodes are visited
            - space: O(n), queue can get as large as n/2 which is the max height of the tree
        """
        new_node = TreeNode(val)

        if not root:
            root = new_node
            return root

        def dfs(root, new_node):
            if not root:
                root = new_node
                return root
            # left
            if new_node.val < root.val:
                root.left = dfs(root.left, new_node)
            # right
            if new_node.val > root.val:
                root.right = dfs(root.right, new_node)
            return root

        def bfs(root, new_node):
            queue = deque([root])
            while queue:
                q_len = len(queue)
                node = queue.popleft()
                for _ in range(q_len):
                    # left
                    if new_node.val < node.val:
                        if node.left:
                            queue.append(node.left)
                        else:
                            node.left = new_node
                    # right
                    if new_node.val > node.val:
                        if node.right:
                            queue.append(node.right)
                        else:
                            node.right = new_node
            return root

        # root = dfs(root,new_node)
        root = bfs(root, new_node)

        return root
