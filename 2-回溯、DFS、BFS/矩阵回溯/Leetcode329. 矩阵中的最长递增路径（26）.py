class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        @cache
        def dfs(i, j):
            cur = 1
            for xi, xj in directions:
                x, y = xi + i, xj + j
                if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
                    cur = max(cur, dfs(x, y) + 1)
            return cur

        res = 0
        for i in range(m):
            for j in range(n):
                if dfs(i, j) > res:
                    res = dfs(i, j)
        return res
