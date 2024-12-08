"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return
        def recursive(node, res):
            if node == None:
                return
            res.append(node.val)
            for i in node.children:
                recursive(i, res)
        res = []
        recursive(root, res)
        return res