"""
@Author: HuKai
@Date: 2022/5/26  9:47
@github: https://github.com/HuKai97
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: return s
        # dp[i][j]表示s[i:j+1]是否是回文子串
        dp = [[False for _ in range(len(s))]for _ in range(len(s))]
        for i in range(len(s)):
           dp[i][i] = True  # 一个字符时都是回文子串
        start, end = 0, 0  # 记录最长子串的起始和终止节点位置
        max_len = 1   # 记录最长子串长度  最短为1
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    # j - i + 1 <= 3
                    if j - i <= 2: dp[i][j] = True
                    else: dp[i][j] = dp[i+1][j-1]
                if dp[i][j] == True and (j-i+1) > max_len:
                    max_len = j - i + 1
                    start = i
                    end = j
        # 进阶 找到所有的最长回文子串
        # res = []
        # if max_len == 0:
        #     for i in range(len(s)):
        #         res.append(s[i])
        # else:
        #     for i in range(len(s)):
        #         for j in range(i+0, len(s)):
        #             if (j-i+0) == max_len and dp[i][j] == True:
        #                 res.append(s[i:j+0])
        # print(res)
        return s[start: end+1]