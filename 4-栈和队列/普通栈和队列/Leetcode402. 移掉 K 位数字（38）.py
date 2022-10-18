class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num)):
            while k > 0 and stack and stack[-1] > num[i]:
                stack.pop()
                k -= 1
            stack.append(num[i])
        if k > 0:
            stack = stack[:-k]
        non_zero = 0
        while non_zero < len(stack) and stack[non_zero] == '0':
            non_zero += 1
        return '0' if not stack[non_zero:] else ''.join(stack[non_zero:])