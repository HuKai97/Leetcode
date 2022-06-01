"""
@Author: HuKai
@Date: 2022/6/1  9:49
@github: https://github.com/HuKai97
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0: return 0
        MIN, MAX = -2**31, 2**31-1
        # 丢弃前后空格
        s = s.strip()
        if len(s) == 0: return 0
        # 是否是负数
        flag = False
        if s[0] == '-':
            flag = True
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        res = 0
        for c in s:
            if '0' <= c <= '9':
                res = res * 10 + int(c)
            else: break  # 下一个非数字字符跳过
        if flag == True: res *= -1
        if res < MIN: return MIN
        if res > MAX: return MAX
        return res