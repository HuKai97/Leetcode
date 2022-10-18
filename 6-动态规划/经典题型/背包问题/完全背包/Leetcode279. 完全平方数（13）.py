class Solution:
    def numSquares(self, n: int) -> int:
        # 完全背包：每个平方数可以使用多次  求最少的平方数个数
        # 物品：1 - floor(sqrt(n))    背包重量：n
        nums = [i * i for i in range(1, floor(sqrt(n)) + 1)]
        dp = [float('inf') for _ in range(n+1)]
        dp[0] = 0
        # print(nums)  # [1, 4, 9]
        for i in range(len(nums)):
            for j in range(nums[i], n+1):
                dp[j] = min(dp[j], dp[j-nums[i]]+1)
        return dp[-1] if dp[-1] != float('inf') else 0