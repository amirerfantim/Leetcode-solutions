class MyQueue:

    def __init__(self):
        self.master = []
        self.slave = []

    def push(self, x: int) -> None:
        self.master.append(x)

    def pop(self) -> int:
        while not self.empty():
            self.slave.append(self.master.pop())
        result = self.slave.pop()
        self.master.append(self.slave.pop())
        return result

    def peek(self) -> int:
        while not self.empty():
            self.slave.append(self.master.pop())
        result = self.slave[-1]
        self.master.append(self.slave.pop())
        return result

    def empty(self) -> bool:
        if len(self.master) == 0:
            return True
        else:
            return False
