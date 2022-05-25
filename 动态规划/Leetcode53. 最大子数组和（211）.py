"""
@Author: HuKai
@Date: 2022/5/25  10:40
@github: https://github.com/HuKai97
"""
# 动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        max_sum = nums[0]
        # dp[i]表示以nums[0]~nums[i]数组的最大子数组和
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            # 加i  不加i
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            if dp[i] > max_sum: max_sum = dp[i]
        return max_sum