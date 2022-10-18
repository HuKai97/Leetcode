class Solution:
    def checkValidString(self, s: str) -> bool:
        # https://leetcode.cn/problems/valid-parenthesis-string/solution/you-xiao-de-gua-hao-zi-fu-chuan-by-leetc-osi3/
        if not s: return True
        left_stack, star_stack = [], []
        for i in range(len(s)):
            if s[i] == '(': left_stack.append(i)
            elif s[i] == '*': star_stack.append(i)
            else:
                if left_stack: left_stack.pop()
                elif star_stack: star_stack.pop()
                else: return False
        while left_stack and star_stack:
            left = left_stack.pop()
            star = star_stack.pop()
            if left > star: return False  # 左括号 必须在对应的右括号之前
        return len(left_stack) == 0