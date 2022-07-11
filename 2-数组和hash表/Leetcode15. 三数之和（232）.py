"""
@Author: HuKai
@Date: 2022/5/25  9:35
@github: https://github.com/HuKai97
"""
# 双指针
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return []
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if nums[i] > 0: break  # 剪枝1 nums[i]>0 后面也必>0 不存在相加为0的组合
            if i > 0 and nums[i] == nums[i-1]: continue  # 剪枝 排除重复元素
            target = 0 - nums[i]
            left, right = i+1, len(nums) - 1
            while left < right:
                cur_sum = nums[left] + nums[right]
                if cur_sum == target and [nums[i], nums[left], nums[right]] not in res:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif cur_sum > target: right -= 1
                else: left += 1
        return res