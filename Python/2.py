# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        result = dummy

        total = carry = 0

        while l1 or l2 or carry:
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next

            total += carry
            number = (total) % 10
            carry = total // 10
            total = 0
            dummy.next = ListNode(number)
            dummy = dummy.next
        return result.next

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
    l1 = create_linked_list([2, 4, 3])
    l2 = create_linked_list([5, 6, 4])

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Result:")
    print_linked_list(result)
