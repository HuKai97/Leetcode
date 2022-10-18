class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board: return False
        m, n = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(i, j, visited, idx):
            # 从board[i][j]开始搜索，看有没有word[idx:]
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[idx]:
                return False
            if idx == len(word) - 1: return True   # idx 0~len(word)-1
            visited.add((i, j))
            for di, dj in directions:
                new_i, new_j = i + di, j + dj
                if (new_i, new_j) not in visited:
                    if dfs(new_i, new_j, visited, idx+1) == True:
                        return True
            visited.remove((i, j))
            return False

        idx = 0
        visited = set()
        for i in range(m):
            for j in range(n):
                if dfs(i, j, visited, idx) == True:
                    return True
        return False