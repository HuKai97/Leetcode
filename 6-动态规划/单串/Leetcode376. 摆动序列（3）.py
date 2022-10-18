class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        # dp[i][0]表示以nums[i]结尾，且最后上升的子序列长度  山峰
        # dp[i][1]表示以nums[i]结尾，且最后下降的子序列长度  山谷
        dp = [[1, 1] for _ in range(len(nums))]
        # dp[0][0], dp[0][1] = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:   # 山峰
                dp[i][0] = dp[i-1][1] + 1
                dp[i][1] = dp[i-1][1]
            elif nums[i] < nums[i-1]:  # 山谷
                dp[i][0] = dp[i-1][0]
                dp[i][1] =  dp[i-1][0]+1
            else:
                dp[i][0] = dp[i-1][0]
                dp[i][1] = dp[i-1][1]
        return max(dp[-1][0], dp[-1][1])