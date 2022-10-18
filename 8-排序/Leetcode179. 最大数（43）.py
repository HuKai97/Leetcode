class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums: return ''
        if len(nums) == 1: return str(nums[0])
        def quick_sort(nums, left, right):
            if left >= right: return
            temp = left
            i, j = left, right
            while i < j:
                # 比较数字的第1位
                # 降序排列
                while i < j and (nums[i]+nums[temp]) > (nums[temp]+nums[i]): i += 1
                while i < j and (nums[j]+nums[temp]) <= (nums[temp]+nums[j]): j -= 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[temp], nums[i] = nums[i], nums[temp]
            quick_sort(nums, left, temp-1)
            quick_sort(nums, temp+1, right)
        nums = list(map(str, nums))  # [10, 2] -> ['10', '2']
        quick_sort(nums, 0, len(nums)-1)
        non_zero_location = 0
        # len(nums) - 0  至少还是要保留一位的  比如'00'最终输出'0'
        while non_zero_location < len(nums) - 1 and nums[non_zero_location] == '0':
            non_zero_location += 1
        return ''.join(nums[non_zero_location:])
