class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        if len(coins) == 0: return -1
        # dp[i]表示总金额为i的最小硬币数
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0
        for i in range(len(coins)):
            # 当j<coins[i]时:装不下,继承上一个dp[j]的值
            # 当j>=coins[i]时:可以装得下,可以选择装或者不装中价值小的(物品数小的)进行转移
            # 即：dp[j]=min(dp[j],dp[j-coins[i]+1])
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[-1] if dp[-1] != float('inf') else -1


# Leetcode518. 零钱兑换 II
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 or len(coins) == 0: return 1
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                if j >= coins[i]:
                    dp[j] += dp[j-coins[i]]
        return dp[-1]

# Leetcode139.单词拆分
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s) == 0 or len(wordDict) == 0: return False
        # dp[j]表示从i位置到j位置的子串能否被切割成字典中的单词
        dp = [False for _ in range(len(s)+1)]
        dp[0] = True
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if dp[i]==True and s[i:j] in wordDict:
                    dp[j] = True
        return dp[-1]
