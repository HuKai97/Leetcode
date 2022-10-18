class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        # dp[i]表示以nums[i]结尾的数组的最长递增子序列的长度
        dp = [1 for _ in range(len(nums))]
        # count[j]表示以nums[i]结尾的数组的最长递增子序列的个数
        count = [1 for _ in range(len(nums))]
        max_len = 1
        res = 0
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i] < dp[j] + 1:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[i] == dp[j] + 1:
                        count[i] += count[j]
            if dp[i] > max_len:
                max_len = dp[i]
                res = count[i]
            elif dp[i] == max_len:
                res += count[i]
        return res