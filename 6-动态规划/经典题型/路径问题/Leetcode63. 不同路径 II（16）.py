# 63. 不同路径 II
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        if m == 0 or n == 0: return 0
        # dp[i][j]表示从00走到ij共多少条路径
        dp = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1: break  # 第一列只要有一个1后面就不需要比较了
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1: break  # 第一行只要有一个1后面就不需要比较了
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]