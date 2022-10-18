class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        # 在stones前面加上+或-  使得式子最小  找到这个最小值
        # sum = pos - neg  ->  pos = sum - neg
        # sum - neg - neg 尽可能的小
        # bagweight = neg = sum // 2  neg就要在不超过sum//2的情况下尽可能的大
        sum_ = sum(stones)
        bagweight = sum_ // 2
        # dp[j]表示在stones[:i]中任选，背包容量为sum//2的情况下 最大的价值
        dp = [0 for _ in range(bagweight + 1)]
        for i in range(len(stones)):
            for j in range(bagweight, stones[i]-1, -1):
                dp[j] = max(dp[j], dp[j-stones[i]]+stones[i])
        return sum_ - 2 * dp[-1]
