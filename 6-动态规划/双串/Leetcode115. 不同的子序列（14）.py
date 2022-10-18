class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m == 0: return 0
        if n == 0: return 1
        if m < n: return 0
        if m == n: return 1 if s == t else 0
        # dp[i][j]表示s[:i+1]中的出现t[:j+1]的子序列个数
        dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
        # 第1行 s为空 => 0   第1列 t为空 => 1
        for i in range(m+1):
            dp[i][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] != t[j-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
        return dp[-1][-1]