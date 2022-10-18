# https://www.programmercarl.com/0134.%E5%8A%A0%E6%B2%B9%E7%AB%99.html#%E8%B4%AA%E5%BF%83%E7%AE%97%E6%B3%95-%E6%96%B9%E6%B3%95%E4%BA%8C
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_sum = 0
        total_sum = 0
        start = 0
        # 局部最优：当前累加rest[j]的和curSum一旦小于0，起始位置至少要是j+1
        # 全局最优：找到可以跑一圈的起始位置
        for i in range(len(gas)):
            cur_sum += gas[i] - cost[i]
            total_sum += gas[i] - cost[i]
            if cur_sum < 0:  # 不能从 ~i开始 要从i+1开始才可能 重新统计cur_sum
                start = i + 1
                cur_sum = 0
        if total_sum < 0: return -1
        return start