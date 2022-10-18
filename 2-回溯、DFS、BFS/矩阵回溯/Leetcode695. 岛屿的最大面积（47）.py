class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0: return 0
        max_area = 0
        def dfs(i, j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j] == 0: return 0
            grid[i][j] = 0
            cur_area = 1
            cur_area += dfs(i-1, j)
            cur_area += dfs(i+1, j)
            cur_area += dfs(i, j+1)
            cur_area += dfs(i, j-1)
            return cur_area
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(dfs(i, j), max_area)
        return max_area