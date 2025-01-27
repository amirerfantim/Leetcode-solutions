# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


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


def print_tree(root):
    if root is None:
        print("Tree is empty")
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.val, end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print()


def test_max_depth(values):
    root = create_tree(values)
    solution = Solution()
    max_depth = solution.maxDepth(root)
    print(f"Tree: {values}")
    print(f"Maximum Depth: {max_depth}")
    print_tree(root)
    print("------------")


while True:
    user_input = input("Enter a list of values for the binary tree (e.g., [3, 9, 20, None, None, 15, 7]): ")

    try:
        tree_values = eval(user_input)

        test_max_depth(tree_values)
    except Exception as e:
        print(f"Invalid input. Error: {e}")

    another_test = input("Do you want to test another tree? (yes/no): ").strip().lower()
    if another_test != 'yes':
        break