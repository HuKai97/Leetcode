class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def dfs(board, res, row):
            if row == n:
                res.append([''.join(r) for r in board])
                return
            for col in range(n):
                if check(board, row, col):  # 遍历每一列
                    board[row][col] = 'Q'
                    dfs(board, res, row + 1)
                    board[row][col] = '.'

        def check(board, row, col):
            for i in range(n):  # 判断同行和同列有没有皇后
                if board[row][i] == 'Q' or board[i][col] == 'Q': return False
            for i in range(n):
                for j in range(n):
                    # 判断同一斜线上有没有皇后
                    if (i + j) == (row + col) and board[i][j] == 'Q': return False
                    if (i - j) == (row - col) and board[i][j] == 'Q': return False
            return True

        board = [['.' for _ in range(n)] for _ in range(n)]
        res = []
        row = 0
        dfs(board, res, row)
        return res