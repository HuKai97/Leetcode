"""
@Author: HuKai
@Date: 2022/5/25  11:22
@github: https://github.com/HuKai97
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return True
        stack = []
        mapp = {'[': ']', '(': ')', '{': '}'}
        for i in range(len(s)):
            if s[i] in mapp: stack.append(s[i])
            else:
                if not stack: return False
                top = stack.pop()
                if mapp[top] != s[i]: return False  # 这里top不可能是 ) ] }
        return False if stack else True

# 678