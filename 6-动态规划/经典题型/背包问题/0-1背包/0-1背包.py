# 0-1背包
# 变形题1、找到重量为j的组合数目？装满背包有几种方法？
# Leetcode494. 目标和（12）
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 设数组中添加'-'元素的总和为neg  则添加'+'的总和为sum_nums-neg
        # (sum_nums-neg) - neg = target => bagweight = neg = (sum_nums-target)//2
        # 所以问题转换为：求出和为bagweight的个数
        sum_nums = sum(nums)
        if (sum_nums - target) % 2 == 1: return 0
        if target > sum_nums: return 0
        bagweight = (sum_nums - target) // 2
        dp = [0 for _ in range(bagweight + 1)]
        dp[0] = 1
        for i in range(len(nums)):  # 遍历物品 重量
            for j in range(bagweight, nums[i]-1, -1):  # 遍历背包容量
                if j >= nums[i]:   # 当前背包容量必须大于当前物品重量
                    dp[j] += dp[j-nums[i]]
        return dp[-1]

# 变形题2、能否找到重量为j的组合？能否装满背包
# Leetcode416、分割等和子集（11）
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2: return False
        if sum(nums) % 2 == 1: return False
        bagweight = sum(nums) // 2
        if max(nums) > bagweight: return False
        # dp[i][j]表示下标0~i的元素任意取，限定背包容量为target的情况下 最终最大价值是多少
        dp = [0 for _ in range(bagweight+1)]
        for i in range(len(nums)):
            for j in range(bagweight, nums[i]-1, -1):
                if j >= nums[i]:
                    # 0、不放i 背包容量为j 最大和为dp[i-0][j]
                    # 2、放i 背包容量为j-nums[i] 最大值为dp[i-0][j-nums[i]]+nums[i]
                    dp[j] = max(dp[j], dp[j-nums[i]]+nums[i])
                # 如果背包容量为bagWeight（目标和），前i个元素任取的情况下最大和恰好等于背包元素
                # 又因为dp[i][bagWeight] <= bagWeight 所以如果有等于的话 那么就满足条件
                if dp[bagweight] == bagweight: return True
        return False