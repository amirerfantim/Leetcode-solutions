# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        first = second = dummy

        for _ in range(n + 1):
            first = first.next
        while first:
            second = second.next
            first = first.next

        second.next = second.next.next
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
    head = create_linked_list([1])

    solution = Solution()
    result = solution.removeNthFromEnd(head, 1)

    print("Result:")
    print_linked_list(result)