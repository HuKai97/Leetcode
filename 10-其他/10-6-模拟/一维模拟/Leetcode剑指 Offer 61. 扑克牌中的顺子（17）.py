class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        if len(nums) != 5: return False
        min_v, max_v = 14, 0
        mapp = []
        for i in range(len(nums)):
            # 除了0意外不能重复  如果重复 一定不是顺子
            if nums[i] in mapp: return False
            # 大小王不用管
            if nums[i] == 0: continue
            min_v = min(min_v, nums[i])
            max_v = max(max_v, nums[i])
            mapp.append(nums[i])
        # 如果最大-最小值<5  就可以形成顺子
        # >5肯定不行  =5  12356肯定不是顺子  <5 12345 12500是顺子
        return max_v - min_v < 5