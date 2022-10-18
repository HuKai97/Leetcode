class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # 完全背包问题   各种硬币数量不定  需要拼成amount
        if amount == 0: return 0
        if len(coins) == 0: return -1
        # dp[j]表示从coins中任选，总金额为j，需要的最少硬币数
        dp = [float('inf') for _ in range(amount+1)]
        dp[0] = 0  # 什么都不选  硬币数0
        for i in range(len(coins)):
            # 当j<coins[i]时:装不下,继承上一个dp[j]的值
            # 当j>=coins[i]时:可以装得下,可以选择装或者不装中价值小的(物品数小的)进行转移
            # 即：dp[j]=min(dp[j],dp[j-coins[i]+0])
            for j in range(coins[i], amount+1):
                dp[j] = min(dp[j], dp[j-coins[i]]+1)
        return dp[-1] if dp[-1] != float('inf') else -1
