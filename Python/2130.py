from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head
        prev = None
        half_len = 0
        res = 0

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            half_len += 1
            prev = slow

        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        fp = head
        sp = prev

        i = 0
        while i < half_len:
            fp_val = fp.val
            sp_val = sp.val
            if fp_val + sp_val > res:
                res = fp.val + sp.val
            sp = sp.next
            fp = fp.next
            i += 1
        return res


def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


input_list = [5, 16, 1, 11, 2, 1]
head = create_linked_list(input_list)

solution = Solution()
result = solution.pairSum(head)

print(result)
