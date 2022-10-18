class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 最多两笔交易
        if len(prices) < 2: return 0
        # dp[i][j][k]: i第几天  j 0 1 是否持股   k 0 1 2目前完成的交易次数
        dp = [[[0 for _ in range(3)]for _ in range(2)]for _ in range(len(prices))]
        dp[0][0][0] = 0
        dp[0][0][1] = float('-inf')  # 不可能事件
        dp[0][0][2] = float('-inf')  # 不可能事件
        dp[0][1][0] = -prices[0]
        dp[0][1][1] = float('-inf')  # 不可能事件
        dp[0][1][2] = float('-inf')  # 不可能事件
        for i in range(1, len(prices)):
            # 第i天 未持股 没卖出去
            dp[i][0][0] = 0
            # 第i天 未持股 卖出一次 = max(今天卖的，以前卖的)
            dp[i][0][1] = max(dp[i-1][1][0]+prices[i], dp[i-1][0][1])
            dp[i][0][2] = max(dp[i-1][1][1]+prices[i], dp[i-1][0][2])
            # 第i天 持股 没卖出去 = max(今天持股，以前持股)
            dp[i][1][0] = max(dp[i-1][0][0]-prices[i], dp[i-1][1][0])
            # 第i天 持股 卖出一次 = max(今天持股，以前持股)
            dp[i][1][1] = max(dp[i-1][0][1]-prices[i], dp[i-1][1][1])
            dp[i][1][2] = float('-inf')  # 不可能事件 最多两次交易
        return max(dp[-1][0][0], dp[-1][0][1], dp[-1][0][2])