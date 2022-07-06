"""
@Author: HuKai
@Date: 2022/5/26  11:24
@github: https://github.com/HuKai97
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums: return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target: return mid
            # 说明左边有序
            if nums[mid] > nums[right]:  # 关于旋转数组问题 都先比较nums[mid]>nums[right]的情况
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # 说明右边有序
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1