class MyCircularQueue:

    def __init__(self, k: int):
        # rear == front  空
        # (rear + 1) % len(queue) == front  满
        self.queue = [0 for _ in range(k+1)]
        self.front = 0
        self.rear = 0

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear + 1) % len(self.queue)
            return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.front = (self.front + 1) % len(self.queue)
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        else: return self.queue[self.front]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        else: return self.queue[(self.rear - 1) % len(self.queue)]

    def isEmpty(self) -> bool:
        return self.front == self.rear

    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.queue) == self.front