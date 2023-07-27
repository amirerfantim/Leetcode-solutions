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
        res = [root.val]
        while len(queue) > 0:
            i = 0
            length = len(queue)
            while i < length:
                i += 1
                cur = queue.popleft()
                if cur.right:
                    queue.append(cur.right)
                if cur.left:
                    queue.append(cur.left)
            if len(queue) > 0:
                res.append(queue[0].val)
        return res