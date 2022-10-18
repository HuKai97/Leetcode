class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums数组可能存在重复元素
        if len(nums) == 1: return nums[0]
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                # 中间数字等于右边数字，比如[2,3,1,1,1]
                # 则重复数字可能为最小值，也可能最小值在重复值的左侧
                # 所以将right左移一位 删除right, 因为删除了也没关系，还有一个mid在
                right -= 1
        return nums[left]