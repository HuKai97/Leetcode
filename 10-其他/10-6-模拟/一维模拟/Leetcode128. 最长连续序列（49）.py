class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        nums_set = set(nums)
        max_len = 1
        for i in range(len(nums)):
            if (nums[i] - 1) not in nums_set:
                cur_start = nums[i]
                cur_len = 1
                while (cur_start + 1) in nums_set:
                    cur_start += 1
                    cur_len += 1
                if cur_len > max_len: max_len = cur_len
        return max_len