class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # 找最大连续的窗口  该窗口内最多有k个0
        res = 0
        start = 0
        count_one = 0
        for end in range(len(nums)):
            if nums[end] == 1:
                count_one += 1
            while count_one + k < end - start + 1:
                if nums[start] == 1:
                    count_one -= 1
                start += 1
            res = max(res, end - start + 1)
        return res