class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def dfs(row, col):
            if row < 0 or row >= m or col < 0 or col >= n or board[row][col] != 'O': return
            board[row][col] = 'A'
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        if not board or m == 1 or n == 1: return
        for i in range(m):
            if board[i][0] == 'O': dfs(i, 0)  # 第一列和最后一列
            if board[i][n-1] == 'O': dfs(i, n - 1)
        for j in range(n):
            if board[0][j] == 'O': dfs(0, j)  # 第一行和最后一行
            if board[m-1][j] == 'O': dfs(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'A':
                    board[i][j] = 'O'