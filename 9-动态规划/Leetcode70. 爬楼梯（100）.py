"""
@Author: HuKai
@Date: 2022/5/27  11:17
@github: https://github.com/HuKai97
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        # dp[i]表示到达第i个台阶有多少种不同的方法
        dp = [0 for _ in range(n+1)]
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[-1]