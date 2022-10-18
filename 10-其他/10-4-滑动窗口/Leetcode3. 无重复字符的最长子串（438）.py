"""
@Author: HuKai
@Date: 2022/5/25  8:43
@github: https://github.com/HuKai97
"""
# 不定长滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        start = 0
        max_len = 1
        mapp = set()
        for end in range(len(s)):
            while s[end] in mapp:
                mapp.remove(s[start])
                start += 1
            mapp.add(s[end])
            max_len = max(max_len, end-start+1)  # 比较一次即可
        return max_len

# 栈
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2: return len(s)
        start = 0
        stack = []
        res = 0
        for end in range(len(s)):
            while s[end] in stack:
                stack.pop(0)
                start += 1
            stack.append(s[end])
            if end - start + 1 > res:
                res = end - start + 1
        return res
# 空间复杂度O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        start = 0
        for end in range(len(s)):
            while s[end] in s[start:end]:
                start += 1
            res = max(res, end - start + 1)
        return res