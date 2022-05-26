"""
@Author: HuKai
@Date: 2022/5/25  10:58
@github: https://github.com/HuKai97
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 只能买卖一次  同一天只能买入或者卖出
        if len(prices) < 2: return 0
        # dp[i][0]: 表示第i天未持股最大的利润
        # dp[i][1]: 表示第i天持股最大的利润
        dp = [[0 for _ in range(2)]for _ in range(len(prices))]
        dp[0][0], dp[0][1] = 0, -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            # dp[i-1][0]只能为0  因为只能买卖一次
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[-1][0]
