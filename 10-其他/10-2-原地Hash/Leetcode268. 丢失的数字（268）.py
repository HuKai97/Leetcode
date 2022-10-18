class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            #
            while nums[i] < n and nums[i] != i:
                nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        # print(nums)
        for i in range(len(nums)):
            if nums[i] != i: return i
        return len(nums)