class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        queue = [root]
        while queue:
            nodes_to_add = []
            for i in range(len(queue)):
                current = queue.pop(0)
                current.next = queue[0] if queue else None
                if current.left:
                    nodes_to_add.append(current.left)
                if current.right:
                    nodes_to_add.append(current.right)
            for node in nodes_to_add:
                queue.append(node)
        return root



