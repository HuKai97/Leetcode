class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 从后往前 找到第一个升序的位置
        i = len(nums) - 2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1
        # 找到nums[i] < nums[i+1]

        # 从后往前 找到第一个比nums[i]大的数
        # 23541 -> 24531    23451 -> 23541
        if i >= 0:  # 321 全降序情况下 i-=1 => i=-1  全降序 没有更大的数了
            j = len(nums) - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # 找到nums[j] < nums[i]
            nums[i], nums[j] = nums[j], nums[i]
        # print(nums[i+1:])
        # 再把nums[i+1:]后面的数升序排列
        # [i+1,end) 必然是降序 翻转 就是升序
        start, end = i + 1, len(nums) - 1
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1