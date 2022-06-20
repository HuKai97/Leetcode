"""
@Author: HuKai
@Date: 2022/5/27  9:15
@github: https://github.com/HuKai97
"""
import copy
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0: return []
        if len(nums) == 1: return [nums]
        def dfs(used, nums, path, res):
            if len(path) == len(nums):
                res.append(copy.deepcopy(path))
                return
            for i in range(len(nums)):
                if nums[i] in used: continue
                used.append(nums[i])
                path.append(nums[i])
                dfs(used, nums, path, res)
                path.pop()
                used.pop()
        used, path, res = [], [], []
        dfs(used, nums, path, res)
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