# 198. 打家劫舍
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        # dp[i]：表示偷窃0~i房间最高的金额
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[-1]

# 213. 打家劫舍 II
class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(nums):
            if len(nums) == 0: return 0
            if len(nums) == 1: return nums[0]
            if len(nums) == 2: return max(nums[0], nums[1])
            dp = [0 for _ in range(len(nums))]
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            res = 0
            for i in range(2, len(nums)):
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])
                res = max(res, dp[i])
            return res
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        val1 = rob_line(nums[1:])
        val2 = rob_line(nums[:-1])
        val3 = rob_line(nums[1:-1])
        return max(val1, val2, val3)