# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root.left and not root.right:
                return [root.val]
            stack = [root]
            leaves = []
            while len(stack) > 0:
                cur = stack.pop()
                if cur.right:
                    stack.append(cur.right)
                if cur.left:
                    stack.append(cur.left)
                if not cur.left and not cur.right:
                    leaves.append(cur.val)
            return leaves

        leaves1 = dfs(root1)
        leaves2 = dfs(root2)
        print(leaves1, leaves2)
        if leaves1 == leaves2:
            return True
        else:
            return False

# Create root1
root1 = TreeNode(3)
root1.left = TreeNode(5)
root1.right = TreeNode(1)
root1.left.left = TreeNode(6)
root1.left.right = TreeNode(2)
root1.right.left = TreeNode(9)
root1.right.right = TreeNode(8)
root1.left.right.left = TreeNode(7)
root1.left.right.right = TreeNode(4)

# Create root2
root2 = TreeNode(3)
root2.left = TreeNode(5)
root2.right = TreeNode(1)
root2.left.left = TreeNode(6)
root2.left.right = TreeNode(7)
root2.right.left = TreeNode(4)
root2.right.right = TreeNode(2)
root2.right.right.right = TreeNode(8)
root2.right.right.right.left = TreeNode(9)

s1 = Solution()
print(s1.leafSimilar(root1, root2))