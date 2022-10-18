class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        # 两次贪心
        # 1、有正有负：这一步让绝对值大的负数变成正数 整体上数组和会最大
        # 2、全是正数：让绝对值最小的数进行取反 整体上数组核会最大
        nums = sorted(nums, key=abs, reverse=True)
        for i in range(len(nums)):
            if nums[i] < 0 and k > 0:
                nums[i] *= -1
                k -= 1
        if k > 0:
            nums[-1] *= (-1) ** k
        return sum(nums)