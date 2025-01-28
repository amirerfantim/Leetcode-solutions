from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(node1, node2):
            if not node1 or not node2:
                return node1 == node2
            return node1.val == node2.val and is_mirror(node1.left, node2.right) and is_mirror(node1.right, node2.left)

        return is_mirror(root.left, root.right)