class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        if len(nums) < 2: return []
        res = []
        for i in range(len(nums)):
            while 1 <= nums[i] <= len(nums) and nums[i]-1 != i and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        for i in range(len(nums)):
            if nums[i] - 1 != i:
                res.append(nums[i])
        return res
