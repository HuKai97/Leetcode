class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 投票法 两类  是多数元素和不是多少元素
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0: res = nums[i]
            count += (1 if res == nums[i] else -1)
        return res