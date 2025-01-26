from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        map = {}

        current = head
        while current:
            map[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            copy = map[current]
            copy.next = map[current.next]
            copy.random = map[current.random]
            current = current.next

        return map[head]
