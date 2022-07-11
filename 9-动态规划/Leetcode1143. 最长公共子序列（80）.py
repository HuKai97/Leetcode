class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        # dp[i][j]表示text1[:i]和text2[:j]的最长公共子序列长度
        # +1 是因为后面dp[i][j]=dp[i-1][j-1]+1  所以这里idx=0就相当于是空字符串
        # '' 和  其他字符串 或 其他字符串和’‘ 的最长公共子序列的长度都是0
        dp = [[0 for _ in range(len(text2)+1)]for _ in range(len(text1)+1)]
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]