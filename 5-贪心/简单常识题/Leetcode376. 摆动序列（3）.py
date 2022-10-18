class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 求峰值
        if len(nums) < 2: return len(nums)
        pre = 0
        res = 1
        for i in range(1, len(nums)):
            cur = nums[i] - nums[i-1]
            if (cur > 0 and pre <= 0) or (cur < 0 and pre >= 0):
                res += 1
                pre = cur
        return res