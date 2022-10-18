class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2: return 0
        # dp[i][j]表示nums1[:i]且以nums[i]结尾的数组和nums2[:j]且以nums2[j]结尾的数组的最长公共子数组长度
        dp = [[0 for _ in range(len(nums2)+1)]for _ in range(len(nums1)+1)]
        max_len = 0
        for i in range(1, len(nums1)+1):
            for j in range(1, len(nums2)+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                # else: dp[i][j] = 0
                if max_len < dp[i][j]: max_len = dp[i][j]
        return max_len