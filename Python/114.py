# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return []
        queue = deque()

        if root.right:
            queue.appendleft(root.right)
            root.right = None
        if root.left:
            queue.appendleft(root.left)
            root.left = None

        current_root = root
        while queue:
            current_root.right = queue[0]
            current_node = queue.popleft()
            if current_node.right:
                queue.appendleft(current_node.right)
                current_node.right = None
            if current_node.left:
                queue.appendleft(current_node.left)
                current_node.left = None
            current_root = current_root.right
        return root

