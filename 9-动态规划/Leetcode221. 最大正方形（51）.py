class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        if m == 0 or n == 0: return 0
        max_edge = 0
        # dp[i][j]表示从matrix[0][0]到matrix[i][j]的最大正方形边长
        dp = [[0 for _ in range(n)]for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    # 这里之所以要合在一起主要是因为需要比较max_edge  不像62那样不需要比较
                    # 如果base case写在外面的话  无法比较max_edge
                    if i == 0 or j == 0: dp[i][j] = 1
                    else: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_edge = max(max_edge, dp[i][j])
        return max_edge ** 2