# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def DFS(root, res):
            if root is None:
                return res
            return max(DFS(root.left, res+1), DFS(root.right, res+1))
        return DFS(root, 0)
