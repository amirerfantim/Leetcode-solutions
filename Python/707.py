class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        current = self.head
        current_idx = 0
        while current:
            if current_idx == index:
                return current.val
            current_idx += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        node.next = self.head
        self.head = node


    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def addAtIndex(self, index: int, val: int) -> None:
        current = self.head
        current_idx = 0
        node = Node(val)
        if index < 0:
            return
        if index == 0:
            self.addAtHead(val)
            return
        while current:
            if current_idx == index - 1:
                node.next = current.next
                current.next = node
            current = current.next
            current_idx += 1


    def deleteAtIndex(self, index: int) -> None:
        current = self.head
        current_idx = 0
        if index < 0:
            return
        if index == 0 and self.head:
            self.head = self.head.next
            return
        while current and current.next:
            if current_idx == index - 1:
                current.next = current.next.next
            current_idx += 1
            current = current.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
