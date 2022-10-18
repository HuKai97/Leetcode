class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 1、二维数组
        if len(nums) < 2: return False  # 小于2没法拆
        if sum(nums) % 2 == 1: return False  # 奇数没法拆
        bagWeight = sum(nums) // 2
        if max(nums) > bagWeight: return False  # 最大数大于一半 不可能有
        #  # dp[i][j]表示nums[0:i]的物品任取，限定背包容量为bagWeight的情况下  最终的最大价值是多少/相加和的最大值（最大和是bagWeight）
        dp = [[0 for _ in range(bagWeight + 1)] for _ in range(len(nums))]
        for j in range(bagWeight, nums[0] - 1, -1):
            dp[0][j] = nums[0]
        for i in range(1, len(nums)):
            for j in range(1, bagWeight + 1):
                if j < nums[i]:
                    dp[i][j] = dp[i - 1][j]  # 容量小于nums[i]
                else:
                    # 1、不放i 背包容量为j 最大和为dp[i-1][j]
                    # 2、放i 背包容量为j-nums[i] 最大值为dp[i-1][j-nums[i]]+nums[i]
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i])
            # 如果背包容量为bagWeight（目标和），前i个元素任取的情况下最大和恰好等于背包元素
            # 又因为dp[i][bagWeight] <= bagWeight 所以如果有等于的话 那么就满足条件
            if dp[i][bagWeight] == bagWeight: return True
        return False

        # 2、一维数组
        if sum(nums) < 2: return False
        if sum(nums) % 2 == 1: return False
        bagweight = sum(nums) // 2
        if max(nums) > bagweight: return False
        dp = [0 for _ in range(bagweight + 1)]
        for i in range(len(nums)):
            for j in range(bagweight, nums[i] - 1, -1):
                # if j >= nums[i]:
                dp[j] = max(dp[j], dp[j - nums[i]] + nums[i])
            if dp[bagweight] == bagweight: return True
        return False

