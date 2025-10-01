# Notes

## Prefix Sum

## Two Pointers

## Sliding Window

- sliding windows are a variation of the two pointer pattern where a left pointer
  denotes the start of the window and a right pointer denotes the end of a window

Fixed window:

```py
left = right = 0
while right < n:
    if right - left + 1 == fixed_window_size:
        result = process(current_window())
        left += 1
    right += 1
```

Dynamic window:

```py
left = right = 0
while right < n:
    while condition is violated:
        left += 1
    result = process(current_window())
    right += 1
```

## Trees

- depth - number of edges from the root to the given node
- height - length with the longest path from the root to a leaf
- maximum depth = height - 1

### DFS

- starting with the root and moving as far down a branch as possible then backtracking
  to explore all other nodes
- recursive
- Time: O(N) all nodes will be visited
- Space: O(N) recursive call stack

#### Preorder Traversal

- used when each node needs to be processed before its children

```py
def dfs(node):
    if not node:
        return
    process(node)
    dfs(node.left)
    dfs(node.right)
```

#### Inorder Traversal

- used when the tree needs to be processed from left to right

```py
def dfs(node):
    if not node:
        return
    dfs(node.left)
    process(node)
    dfs(node.right)
```

#### Postorder Traversal

- used when each subtree needs to be processed before their root

```py
def dfs(node):
    if not node:
        return
    dfs(node.left)
    dfs(node.right)
    process(node)
```

#### Iterative DFS

```py
def dfs(root):
    if not root:
        return
    stack = []
    stack.append(root)
    while stack:
        node = stack.pop()
        process(node)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
```

### BFS

- traverses the tree level by level
- implemented iteratively using a queue
- Time: O(N) every node is visited
- Space: O(N) the queue might get as large as N/2

```py
def bfs(root):
    if not root:
        return
    queue = deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        process(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```
