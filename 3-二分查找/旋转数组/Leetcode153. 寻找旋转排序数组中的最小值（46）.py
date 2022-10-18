class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 数组元素互不相同
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 中间数字大于右边数字，比如[3,4,5,1,2]，则左侧是有序上升的，最小值在右侧
            if nums[mid] > nums[right]:  # 左边有序 说明最小值肯定在右边
                left = mid + 1
            # 中间数字小于等于右边数字，比如[6,7,1,2,3,4,5]，则右侧是有序上升的，最小值在左侧+mid
            else:   # 说明右边有序  最小值在左边+mid
                right = mid
        return nums[left]