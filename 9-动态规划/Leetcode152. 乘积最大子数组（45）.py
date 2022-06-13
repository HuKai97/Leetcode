class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        # dp_max[i]表示以nums[i]为结尾的子数字的最大乘积
        # dp_min[i]表示以nums[i]为结尾的子数字的最大乘积
        dp_max = [nums[i] for i in range(len(nums))]
        dp_min = [nums[i] for i in range(len(nums))]
        max_mul = nums[0]
        for i in range(1, len(nums)):
            dp_max[i] = max(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
            dp_min[i] = min(nums[i], dp_max[i-1]*nums[i], dp_min[i-1]*nums[i])
            max_mul = max(max_mul, dp_max[i], dp_min[i])
        return max_mul