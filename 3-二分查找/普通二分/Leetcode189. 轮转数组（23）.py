class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 找到旋转数组
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        k %= len(nums)
        if k == 0 or len(nums) < 2: return
        reverse(0, len(nums) - 1)    # [1,2,3,4,5,6,7] -> [7,6,5,4,3,2,1]
        reverse(0, k - 1)            # -> [5,6,7,4,3,2,1]
        reverse(k, len(nums) - 1)    # -> [5,6,7,1,2,3,4]