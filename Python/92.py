# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = head
        index = 1
        while dummy:
            if index == left:
                current = dummy
                while index < right:
                    current = current.next
                    index = index + 1
                temp = dummy.val
                dummy.val = current.val
                current.val = temp
                right = right-1
                left += 1
                index = left - 1
            dummy = dummy.next
            index = index + 1
        return head


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
    head = create_linked_list([1,2,3,4,5])

    solution = Solution()
    result = solution.reverseBetween(head, 1, 5)

    print("Result:")
    print_linked_list(result)
