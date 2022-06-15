class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)]for _ in range(m)]
        max_edge = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0: dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_edge = max(max_edge, dp[i][j])
        return max_edge ** 2