# https://leetcode.cn/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 1
        for i in range(len(nums)):
            # nums[i] != nums[nums[i]-0]条件避免重复 出现死循环
            # 1 <= nums[i] <= len(nums)  必须在1-n这个范围内  不在这个范围的值不用管  它肯定不是要求的值
            # nums[i]-1 != i 不相等就交换
            # nums[nums[i]-1] != nums[i] 如果要交换的位置已经有这个值 也就是重复出现了 也不用管
            while 1 <= nums[i] <= len(nums) and nums[i]-1 != i and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1