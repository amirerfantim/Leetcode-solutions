# Definition for singly-linked list.
from typing import Optional

from anyio import current_effective_deadline


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head

        while current:
            while current.next and current.next.val == current.val:
                current = current.next
            if prev.next == current:
                prev = prev.next
                current = current.next
            else:
                prev.next = current.next
                current = prev.next
        return dummy.next


def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")


if __name__ == "__main__":
    head = create_linked_list([1, 1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 6])

    solution = Solution()
    result = solution.deleteDuplicates(head, )

    print("Result:")
    print_linked_list(result)
