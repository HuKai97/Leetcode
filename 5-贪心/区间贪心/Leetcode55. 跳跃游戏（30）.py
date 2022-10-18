class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # https://leetcode.cn/problems/jump-game/solution/tiao-yue-you-xi-by-leetcode-solution/
        max_len = 0
        for i in range(len(nums)):
            if i > max_len: return False
            max_len = max(max_len, nums[i]+i)
            if max_len >= len(nums) - 1: return True
        return True
