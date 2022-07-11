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
            max_len = max(max_len, end-start+1)
        return max_len