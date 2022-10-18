class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if target > sum_nums: return 0
        # neg   pos = sum_nums - neg   target = pos - neg = sum_nums - neg - neg
        # neg = (sum_nums - target) // 2
        if (sum_nums - target) % 2 == 1: return 0
        bagWeight = (sum_nums - target) // 2
        # dp[j]表示从nums[:i]中任选 重量为j的物品 最多多少种不同的方法
        dp = [0 for _ in range(bagWeight + 1)]
        # 从nums中随机挑选物品 重量为0的数量=1种 什么也不装
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(bagWeight, nums[i]-1, -1):
                # 如果背包里已经有一个数nums[i]，那么背包的容量就变成了j-nums[i]，所以在这种情况下还要装满背包就还有dp[j-nums[i]]个方法。
                # 那么对于每个nums[i]，dp[j]+=dp[j-nums[i]]，就可以找到用nums里的所有元素装满容量为j的背包的所有方法数
                dp[j] += dp[j-nums[i]]
        return dp[-1]