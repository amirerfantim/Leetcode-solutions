# Definition for a binary tree node

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        mapping_inorder = {inorder[i]: i for i in range(len(inorder))}
        post_index = [len(postorder) - 1]

        def build(left, right):
            if left > right:
                return None
            root = TreeNode(postorder[post_index[0]])
            mid = mapping_inorder[root.val]
            post_index[0] -= 1

            root.right = build(mid + 1, right)
            root.left = build(left, mid)
            return root
        return build(0, len(inorder) - 1)
