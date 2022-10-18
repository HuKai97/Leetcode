class CQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def appendTail(self, value: int) -> None:
        self.stack2.append(value)



    def deleteHead(self) -> int:
        if not self.stack1 and not self.stack2: return -1
        if self.stack1: return self.stack1.pop()
        else:
            while self.stack2:
                self.stack1.append(self.stack2.pop())
            return self.stack1.pop()