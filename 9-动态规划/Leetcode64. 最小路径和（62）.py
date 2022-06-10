class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0: return 0
        # dp[i][j]表示从dp[0][0]走到dp[i][j]最小路径和
        dp = copy.deepcopy(grid)
        for i in range(1, m):
            dp[i][0] += dp[i-1][0]
        for j in range(1, n):
            dp[0][j] += dp[0][j-1]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += min(dp[i][j-1], dp[i-1][j])
        return dp[-1][-1]