class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) < 2: return 0
        # dp[i][j][t]  i: 第i天  j: 0不持股 1持股   t: 当前完成t笔交易
        dp = [[[0 for _ in range(k+1)]for _ in range(2)]for _ in range(len(prices))]
        # base case
        dp[0][0][0] = 0
        dp[0][1][0] = -prices[0]
        for i in range(1, k+1):
            dp[0][0][i] = float('-inf')
            dp[0][1][i] = float('-inf')
        # 遍历
        for i in range(1, len(prices)):
            for j in range(k+1):
                if j == 0:
                    dp[i][0][0] = 0
                    dp[i][1][0] = max(dp[i-1][1][0], dp[i-1][0][0]-prices[i])
                else:
                    dp[i][0][j] = max(dp[i-1][0][j], dp[i-1][1][j-1]+prices[i])
                    dp[i][1][j] = max(dp[i-1][1][j], dp[i-1][0][j]-prices[i])
        res = 0
        for i in range(k+1):
            res = max(res, dp[-1][0][i])
        return res