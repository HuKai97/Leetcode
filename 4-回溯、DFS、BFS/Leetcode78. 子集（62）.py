class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        def dfs(start, path, res):
            # 不需要任何判断 进来了就肯定是它的子集
            res.append(copy.deepcopy(path))
            for i in range(start, len(nums)):
                path.append(nums[i])
                # i+1：防止出现112 223的情况  一个元素重复使用
                dfs(i+1, path, res)
                path.pop()
        start = 0
        path, res = [], []
        dfs(start, path, res)
        return res



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