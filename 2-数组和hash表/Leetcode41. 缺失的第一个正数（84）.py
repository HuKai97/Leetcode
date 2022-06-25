# https://leetcode.cn/problems/first-missing-positive/solution/que-shi-de-di-yi-ge-zheng-shu-by-leetcode-solution/
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 1
        for i in range(len(nums)):
            # nums[i] != nums[nums[i]-1]条件避免重复 出现死循环
            while 1 <= nums[i] <= len(nums) and nums[i]-1 != i and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1