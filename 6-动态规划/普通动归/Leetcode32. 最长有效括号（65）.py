# 难
# 视频学习：https://www.bilibili.com/video/BV1MZ4y1B7fB?from=search&seid=8232076784487285058&spm_id_from=333.337.0.0%2F&vd_source=5f6bbc1038b075757cb446f800f3cd56
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) < 2: return 0
        # dp[i]表示以s[i]结尾的字符串最长有效括号长度
        dp = [0 for _ in range(len(s))]
        max_len = 0
        for i in range(1, len(s)):
            if s[i] == '(': dp[i] = 0
            else:
                if s[i-1] == '(': dp[i] = dp[i-2] + 2
                elif s[i-dp[i-1]-1] == '(' and (i-dp[i-1]-1)>=0:
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
            if dp[i] > max_len: max_len = dp[i]
        return max_len