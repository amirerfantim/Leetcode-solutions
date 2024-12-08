class ListNode:
     def __init__(self, val=0, next = None):
         self.val = val
         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        counter = 0
        res = 0
        main_head = head
        while head.next is not None:
            head = head.next
            counter += 1
        while main_head is not None:
            if main_head.val:
                res += pow(2, counter)
            counter -= 1
            main_head = main_head.next
        return res