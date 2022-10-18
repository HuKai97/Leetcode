class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1], [1]
        cur = 1
        for i in range(1, len(nums)):
            cur *= nums[i-1]
            left.append(cur)
        # print(left)
        cur = 1
        for i in range(len(nums)-2, -1, -1):
            cur *= nums[i+1]
            right.append(cur)
        right = right[::-1]
        # print(right)
        for i in range(len(left)):
            left[i] *= right[i]
        return left