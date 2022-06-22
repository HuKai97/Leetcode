"""
@Author: HuKai
@Date: 2022/5/27  10:42
@github: https://github.com/HuKai97
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        # dp[i]表示以i结尾的子序列的最长递增子序列
        dp = [1 for _ in range(len(nums))]
        res = 0
        for i in range(1, len(nums)):
            for j in range(i):
                # 对每个元素都要从前面的元素开始找 找比当前元素小的元素
                # 得到可能的最长子序列长度=dp[j]+1
                # 不确定最长的子序列是哪个  所以要一个个比较
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j]+1, dp[i])
            res = max(res, dp[i])
        return res


# 674. 最长连续递增序列
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        # dp[i]表示以nums[i]结尾的数组的最长连续递增序列长度
        dp = [1 for _ in range(len(nums))]
        res = 0
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                dp[i] = dp[i-1] + 1
            res = max(res, dp[i])
        return res