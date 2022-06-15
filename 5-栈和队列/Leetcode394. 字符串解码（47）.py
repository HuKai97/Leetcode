class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        mutli = 0
        res = ''
        for c in s:
            if 'a' <= c <= 'z':
                res += c
            elif '0' <= c <= '9':
                mutli = mutli * 10 + int(c)
            elif c == '[':
                stack.append([mutli, res])  # 重复次数 和 重复元素前的所有东西
                mutli, res = 0, ''
            else:
                # ']'
                cur_mutli, last_res = stack.pop()
                res = last_res + cur_mutli * res
        return res