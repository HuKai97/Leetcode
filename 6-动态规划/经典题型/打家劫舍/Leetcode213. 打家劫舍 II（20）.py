class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob_line(num):
            n = len(num)
            if n == 0: return 0
            if n == 1: return num[0]
            dp = [0 for _ in range(n)]
            dp[0] = num[0]
            dp[1] = max(num[0], num[1])
            for i in range(2, n):
                dp[i] = max(dp[i-2] + num[i], dp[i-1])
            return dp[-1]
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])
        n1 = rob_line(nums[1:])
        n2 = rob_line(nums[:-1])
        n3 = rob_line(nums[1:-1])
        return max(n1, n2, n3)