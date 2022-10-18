# 39. 组合总和
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if not candidates: return []
        def dfs(start, path, res, target):
            if target == 0:
                res.append(copy.deepcopy(path))
                return
            for i in range(start, len(candidates)):
                if candidates[i] <= target:
                    path.append(candidates[i])
                    dfs(i, path, res, target-candidates[i])
                    path.pop()
        start = 0
        path, res = [], []
        dfs(start, path, res, target)
        return res


