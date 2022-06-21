"""
@Author: HuKai
@Date: 2022/5/27  11:32
@github: https://github.com/HuKai97
"""
# 完完全全是一个二分查找模板题，很简单
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums or target < nums[0] or target > nums[-1]: return -1
        if nums[0] > target or nums[-1] < target: return -1
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else: right = mid
        return left if nums[left] == target else -1