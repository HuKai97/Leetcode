# 前缀和
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        mapp = defaultdict(int)
        mapp[0] = 1
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum - k in mapp: res += mapp[cur_sum-k]
            mapp[cur_sum] += 1
        return res