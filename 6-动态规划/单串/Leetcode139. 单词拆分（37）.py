class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0 or not wordDict: return False
        # dp[i]表示s[:i+1]是否可以被拆分
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(i):
                if dp[j] == True and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]