# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []

        while queue:
            result.append(queue[-1].val)
            child_queue = deque()
            while queue:
                current = queue.popleft()
                if current.left:
                    child_queue.append(current.left)
                if current.right:
                    child_queue.append(current.right)
            queue = child_queue
        return result
