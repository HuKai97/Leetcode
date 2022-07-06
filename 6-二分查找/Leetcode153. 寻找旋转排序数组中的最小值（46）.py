class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:  # 左边有序 说明最小值肯定在右边
                left = mid + 1
            else:   # 说明右边有序  最小值在左边+mid
                right = mid
        return nums[left]