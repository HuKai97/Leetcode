class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 2: return 1
        # dp[i]表示将正整数i拆分成k个正整数，最大乘积
        dp = [0 for _ in range(n+1)]
        # dp[0]和dp[1]没用意义
        dp[2] = 1  # 1 1
        for i in range(3, n+1):
            for j in range(1, i):
                # dp[i] 历史的最大值
                # j * (i-j) 拆分成两个正整数
                # j * (i-j) 拆分成两个以上的正整数
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[-1]