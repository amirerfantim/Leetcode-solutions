from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# Function to create a binary tree from a list of values
def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


# Function to test if two trees are the same
def test_is_same_tree(values_p, values_q):
    tree_p = create_tree(values_p)
    tree_q = create_tree(values_q)

    solution = Solution()
    result = solution.isSameTree(tree_p, tree_q)

    print(f"Tree P: {values_p}")
    print(f"Tree Q: {values_q}")
    print(f"Are both trees the same? {result}")
    print("------------")


# Harde-coded input values
test_is_same_tree([1, 2, 3], [1, 2, 3])  # Example 1 (same trees)
test_is_same_tree([1, 2], [1, None, 2])  # Example 2 (different trees)
test_is_same_tree([1, 2, 3], [1, 2])  # Example 3 (different structures)
test_is_same_tree([], [])  # Example 4 (both empty trees)
test_is_same_tree([1], [1])  # Example 5 (single node trees)
