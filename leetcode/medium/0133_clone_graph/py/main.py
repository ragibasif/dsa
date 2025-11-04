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
* Problem: 0133 - clone_graph
* Platform: leetcode
* Difficulty: medium
* URL: https://leetcode.com/problems/clone-graph/description/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        """
        Notes:
        - deep copy - make a completely new instance of the object (no references)
        - keep a visited hashmap where the og node is the key and the clone node is the value
        - dfs: time O(V + E), space O(V + E)
        - bfs: time O(V + E), space O(V + E)
        """
        if not node:
            return node

        def dfs(node, visited):
            cnode = Node()

            if node in visited:
                return visited[node]

            visited[node] = cnode

            if not node:
                return cnode

            cnode.val = node.val

            for item in node.neighbors:
                cnode.neighbors.append(dfs(item, visited))

            return cnode

        def bfs(node):
            visited = {}
            queue = deque([node])
            while queue:
                cnode = Node()
                og_node = queue.popleft()
                cnode.val = og_node.val
                for item in og_node.neighbors:
                    if item in visited:
                        cnode.neighbors.append(visited[item])
                        flag = False
                        for i in visited[item].neighbors:
                            if i.val == cnode.val:
                                flag = True
                        if not flag:
                            visited[item].neighbors.append(cnode)
                    else:
                        queue.append(item)
                visited[og_node] = cnode
            return visited[node]

        # res = dfs(node,{})
        res = bfs(node)

        return res
