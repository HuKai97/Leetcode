class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def quick_sort(nums, left, right):
            if left >= right: return
            temp = left
            i, j = left, right
            while i < j:
                # 为什么j在前？
                while i < j and (nums[j] + nums[temp]) >= (nums[temp] + nums[j]): j -= 1
                while i < j and (nums[i] + nums[temp]) <= (nums[temp] + nums[i]): i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[temp], nums[i] = nums[i], nums[temp]
            quick_sort(nums, left, i - 1)
            quick_sort(nums, i + 1, right)
        if not nums: return ''
        nums = [str(num) for num in nums]
        quick_sort(nums, 0, len(nums) - 1)
        return ''.join(nums)
