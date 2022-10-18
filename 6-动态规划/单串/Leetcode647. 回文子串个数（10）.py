class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) == 1: return 1
        res = 0
        dp = [[False for _ in range(len(s))]for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
            res += 1
        for i in range(len(s)-2, -1, -1):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    if j - i + 1 <= 3: dp[i][j] = True
                    else: dp[i][j] = dp[i+1][j-1]
                if dp[i][j] == True: res += 1
        return res