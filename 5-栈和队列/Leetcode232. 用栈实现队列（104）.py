"""
@Author: HuKai
@Date: 2022/5/28  9:07
@github: https://github.com/HuKai97
"""
# https://www.bilibili.com/video/BV1W5411L7jC?spm_id_from=333.337.search-card.all.click
class MyQueue:

    def __init__(self):
        # 栈：先进后出
        # 队列：先进先出
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self) -> int:
        if self.stack_out:
            return self.stack_out[-1]
        else:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out[-1]

    def empty(self) -> bool:
        return not self.stack_in and not self.stack_out


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()