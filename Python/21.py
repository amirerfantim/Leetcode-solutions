# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        dummy = head

        while list1 or list2:
            if not list1:
                while list2:
                    dummy.next = ListNode(list2.val)
                    list2 = list2.next
                    dummy = dummy.next
            elif not list2:
                while list1:
                    dummy.next = ListNode(list1.val)
                    list1 = list1.next
                    dummy = dummy.next
            elif list1.val < list2.val:
                dummy.next = ListNode(list1.val)
                list1 = list1.next
                dummy = dummy.next
            elif list1.val >= list2.val:
                dummy.next = ListNode(list2.val)
                list2 = list2.next
                dummy = dummy.next
        return head.next


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
    l1 = create_linked_list([-9, 3])
    l2 = create_linked_list([5, 7])

    solution = Solution()
    result = solution.mergeTwoLists(l1, l2)

    print("Result:")
    print_linked_list(result)
