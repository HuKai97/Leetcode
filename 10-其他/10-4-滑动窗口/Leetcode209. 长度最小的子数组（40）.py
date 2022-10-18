class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums: return 0
        res = len(nums) + 1
        start = 0
        cur_sum = 0
        for end in range(len(nums)):
            cur_sum += nums[end]   # 每改变一次都比较一次
            while cur_sum >= target:
                res = min(res, end-start+1)
                cur_sum -= nums[start]
                start += 1
        return res if res != len(nums) + 1 else 0