# 90. 子集 II
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        def dfs(start, path, res, nums):
            res.append(copy.deepcopy(path))
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]: continue
                path.append(nums[i])
                dfs(i+1, path, res, nums)
                path.pop()
        nums.sort()
        start, path, res = 0, [], []
        dfs(start, path, res, nums)
        return res