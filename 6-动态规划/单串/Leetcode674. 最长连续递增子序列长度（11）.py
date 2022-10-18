class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        dp = [1 for _ in range(len(nums))]
        # dp[0] = 1
        res = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                dp[i] = max(dp[i], dp[i-1]+1)
            res = max(res, dp[i])
        return res