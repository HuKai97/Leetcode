"""
@Author: HuKai
@Date: 2022/5/27  9:49
@github: https://github.com/HuKai97
"""
# 模拟加法
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # 模拟加法
        if not num1: return num2
        if not num2: return num1
        res = []
        add = 0
        i, j = len(num1) - 1, len(num2) - 1
        # add != 0是为了防止1 9 生成10  add=1 但是i=-1 j=-1 所以还要继续执行一次
        while i >= 0 or j >= 0 or add != 0:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            cur_sum = x + y + add
            res.append(str(cur_sum % 10))
            add = cur_sum // 10
            i -= 1
            j -= 1
        # 从后往前append的 所以要-1
        return ''.join(res[::-1])