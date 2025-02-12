# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, target):
            if not node:
                return False
            target -= node.val
            if target < 0:
                return False
            return target == 0 or dfs(node.left, target) or dfs(node.right, target)
        return dfs(root, targetSum)
