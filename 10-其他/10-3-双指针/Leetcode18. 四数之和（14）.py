class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return []
        res = []
        nums.sort()
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]: continue  # i去重
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]: continue  # j去重
                # two sum
                t = target - nums[i] - nums[j]
                left, right = j + 1, len(nums) - 1
                while left < right:
                    cur = nums[left] + nums[right]
                    if cur == t:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left-1]: left += 1  # left去重
                        right -= 1
                        while left < right and nums[right] == nums[right+1]: right -= 1  # right去重
                    elif cur > t: right -= 1
                    else: left += 1
        return res