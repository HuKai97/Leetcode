class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 异或运算  a^0=a   a^a=0  a^b^c=a^c^b
        res = nums[0]
        for i in range(1, len(nums)):
            res ^= nums[i]
        return res