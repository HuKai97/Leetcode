"""
@Author: HuKai
@Date: 2022/5/27  9:15
@github: https://github.com/HuKai97
"""
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        def dfs(path, res, used):
            if len(path) == len(nums):
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if used[i] == True: continue
                used[i] = True
                path.append(nums[i])
                dfs(path, res, used)
                path.pop()
                used[i] = False
        path, res = [], []
        used = [False] * len(nums)
        dfs(path, res, used)
        return res



# 47、全排列 II
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        def dfs(path, res, nums, used):
            if len(path) == len(nums):
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if used[i] == True: continue
                if i > 0 and nums[i] == nums[i-1] and used[i-1] == True:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(path, res, nums, used)
                used[i] = False
                path.pop()
        path, res = [], []
        nums.sort()
        used = [False] * len(nums)
        dfs(path, res, nums, used)
        return res