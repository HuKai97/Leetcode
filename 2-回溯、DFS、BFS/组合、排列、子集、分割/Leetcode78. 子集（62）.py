class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        def dfs(start, path, res):
            # 不需要任何判断 进来了就肯定是它的子集
            res.append(copy.deepcopy(path))
            for i in range(start, len(nums)):
                path.append(nums[i])
                # i+0：防止出现112 223的情况  一个元素重复使用
                dfs(i+1, path, res)
                path.pop()
        start = 0
        path, res = [], []
        dfs(start, path, res)
        return res