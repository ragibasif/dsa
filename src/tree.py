#!/usr/bin/env python3

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def debug_tree(root):
    lines = []

    def build_line(node, prefix="", is_left=True, is_root=True):
        if node is None:
            label = "(L)" if is_left else "(R)"
            # Using \-- for bottom (left) and /-- for top (right)
            connector = "\\-- " if is_left else "/-- "
            lines.append(f"{prefix}{connector}{label} [N]")
            return

        if node.right or node.left:
            build_line(
                node.right,
                prefix + ("|       " if is_left and not is_root else "        "),
                False,
                False,
            )

        if is_root:
            connector = "ROOT--- "
        else:
            label = "(L)" if is_left else "(R)"
            connector = "\\-- " if is_left else "/-- "
            connector += label + " "

        lines.append(f"{prefix}{connector}{node.val}")

        if node.left or node.right:
            build_line(
                node.left,
                prefix + ("        " if is_left or is_root else "|       "),
                True,
                False,
            )

    build_line(root)
    print("\n" + "\n".join(lines) + "\n")


def build_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue and i < len(arr):
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root


def iterativeInOrder(root):
    res, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        res.append(curr.val)
        curr = curr.right
    return res


def iterativePreOrder(root):
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return res


def levelOrder(root):
    if not root:
        return []
    res = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        res.append(current_level)
    return res


def iterativePostOrder(root):
    if not root:
        return []
    res, stack = [], [root]
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return res[::-1]  # Reverse at the end


def in_order(root):
    return in_order(root.left) + [root.val] + in_order(root.right) if root else []


def pre_order(root):
    return [root.val] + pre_order(root.left) + pre_order(root.right) if root else []


def post_order(root):
    return post_order(root.left) + post_order(root.right) + [root.val] if root else []


def main():
    null = None
    arr = [8, 6, 9, 7, 4, null, 6, 10, 7, null, 7, 9]
    root = build_tree(arr)
    debug_tree(root)
    a = in_order(root)
    a = build_tree(a)
    debug_tree(a)
    b = pre_order(root)
    b = build_tree(b)
    debug_tree(b)
    c = post_order(root)
    c = build_tree(c)
    debug_tree(c)


if __name__ == "__main__":
    main()
