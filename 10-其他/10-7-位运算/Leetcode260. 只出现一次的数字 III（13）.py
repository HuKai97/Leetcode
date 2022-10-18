class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        if len(nums) == 2: return nums
        num = 0
        for i in range(len(nums)):
            num ^= nums[i]
        # print(num)  110

        # 找到num右边第一个1
        mask = 1  # 001
        while num & mask == 0:
            mask <<= 1

            # 把3和5分在两个组
        res = [0, 0]
        for n in nums:
            if n & mask == 0:
                res[0] ^= n
            else:
                res[1] ^= n
        return res