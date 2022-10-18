class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, path, res):
            if len(path) == k:
                res.append(copy.deepcopy(path))
                return
            for i in range(start, n+1):
                path.append(i)
                dfs(i+1, path, res)
                path.pop()
        start = 1
        path, res = [], []
        dfs(start, path, res)
        return res