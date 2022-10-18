class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums) == 3: return nums[0]+nums[1]+nums[2]
        nums.sort()  # 不要忘了sort  因为这里用到了双指针的解法 必须有序
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i+1, len(nums)-1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum-target) < abs(res-target):
                    res = cur_sum
                if cur_sum == target: return cur_sum
                elif cur_sum > target: right -= 1
                else: left += 1
        return res