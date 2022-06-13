class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        max_val = max(nums[0], nums[1])
        # dp[i]：表示偷窃0~i房间最高的金额
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
            if max_val < dp[i]: max_val = dp[i]
        return max_val