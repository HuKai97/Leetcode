class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) < 2: return len(s)
        # dp[i][j]表示s[i:j]中最长回文子序列的长度
        dp = [[0 for _ in range(len(s))]for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = 1
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i+1][j])
        return dp[0][-1]