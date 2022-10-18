class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1: return []
        def dfs(res, path, left, right):
            if left == n and right == n:
                res.append(copy.deepcopy(path))
                return
            if left < n:
                dfs(res, path+'(', left+1, right)
            if left > right:
                dfs(res, path+')', left, right+1)
        res, path = [], ''
        left, right = 0, 0
        dfs(res, path, left, right)
        return res