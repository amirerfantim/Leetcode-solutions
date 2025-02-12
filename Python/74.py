# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        result = [float]
        while queue:
            node_sum = 0
            number_of_nodes = len(queue)
            child_level = deque()
            while queue:
                node = queue.pop()
                node_sum += node.val
                if node.left:
                    child_level.append(node.left)
                if node.right:
                    child_level.append(node.right)
            result.append(node_sum / number_of_nodes)
            queue = child_level
        return result
