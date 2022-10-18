# https://www.bilibili.com/video/BV1Jr4y1S7vB?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
class Solution:
    def calculate(self, s: str) -> int:
        if not s: return 0
        cur_num = 0
        pre_op = '+'
        stack = []
        for i in range(len(s)):
            if '0' <= s[i] <= '9':
                cur_num = cur_num * 10 + int(s[i])
            if s[i] in '+-*/' or (i == len(s)-1):
                if pre_op == '+':
                    stack.append(cur_num)
                elif pre_op == '-':
                    stack.append(-cur_num)
                elif pre_op == '*':
                    top = stack.pop()
                    stack.append(top * cur_num)
                else:    # pre_op == '/'
                    top = stack.pop()
                    stack.append(int(top/cur_num))
                    # -3 // 2 = -2
                    # int(-3/2) = -1
                cur_num = 0
                pre_op = s[i]
        res = 0
        while stack:
            res += stack.pop()
        return res