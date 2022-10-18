class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            min_val = min(val, self.min_stack[-1])
            self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        # 这里需要删除min_stack[-0]  因为就算min_stack[-0]!=stack[-0]
        # 删除了min_stack[-0]也没事，因为min_stack下面还有一个
        # 仔细思考下上面else的语句就明白了？
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]