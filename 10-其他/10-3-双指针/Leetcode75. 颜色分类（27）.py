# https://www.bilibili.com/video/BV1tz4y1o7n5?spm_id_from=333.337.search-card.all.click
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = 0
        two = len(nums) - 1
        i = 0
        while i <= two:
            if nums[i] == 0:
                # 交换后的nums[i]肯定=1 不需要比较 i++
                nums[i], nums[zero] = nums[zero], nums[i]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                # 交换后的nums[i]不知道是什么数 需要重新比较 i不变
                nums[i], nums[two] = nums[two], nums[i]
                two -= 1
