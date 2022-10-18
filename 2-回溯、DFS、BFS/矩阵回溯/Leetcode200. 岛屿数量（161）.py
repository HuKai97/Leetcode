"""
@Author: HuKai
@Date: 2022/5/26  9:22
@github: https://github.com/HuKai97
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        if m == 0 or n == 0: return 0
        res = 0
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0': return
            grid[i][j] = '0'
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j-1)
            dfs(i, j+1)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    res += 1
                    dfs(i, j)
        return res