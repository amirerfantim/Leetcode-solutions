# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

from pygments.lexers import q


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        mapping_inorder = {inorder[i]: i for i in range(len(inorder))}
        preorder = deque(preorder)

        def build(left, right) -> Optional[TreeNode]:
            if left > right:
                return None
            root = TreeNode(preorder.popleft())
            mid = mapping_inorder[root.val]
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        return build(0, len(preorder) - 1)


