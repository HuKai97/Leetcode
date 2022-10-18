"""
@Author: HuKai
@Date: 2022/5/25  9:44
@github: https://github.com/HuKai97
"""
# hash map
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 第一想法是和三数之和一样用双指针 但是这里返回的是idx 所以不能sort 也就不能用双指针了
        if len(nums) < 1: return []
        mapp = {nums[0]: 0}
        for i in range(1, len(nums)):
            if target - nums[i] in mapp:
                return [i, mapp[target - nums[i]]]
            mapp[nums[i]] = i


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if not nums: return [-1, -1]
        mapp = []
        for i in range(len(nums)):
            if target - nums[i] in mapp:
                return [i, mapp.index(target-nums[i])]
            mapp.append(nums[i])
        return [-1, -1]