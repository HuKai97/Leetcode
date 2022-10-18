class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while nums[i] != i:
                if nums[nums[i]] == nums[i]: return nums[i]
                else:
                    nums[nums[i]], nums[i] = nums[i], nums[nums[i]]