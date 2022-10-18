# Leetcode518. 零钱兑换 II
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0 or len(coins) == 0: return 1
        # dp[j]表示从amount中任选，总金额为amount的方式多少种
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1  # 什么都不选  1种方案
        for i in range(len(coins)):
            for j in range(coins[i], amount+1):
                dp[j] += dp[j-coins[i]]
        return dp[-1]
