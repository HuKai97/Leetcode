class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3: return 0
        nums.sort()
        res = 0
        for i in range(len(nums)-2):  # a
            if nums[i] <= 0: continue  # 边长必须大于0
            for j in range(i+1, len(nums)-1):  # b
                cur_sum = nums[i] + nums[j]
                if nums[j+1] >= cur_sum: continue  # min(c) >= a+b  跳过
                left, right = j + 1, len(nums) - 1
                # 找到满足 c<a+b 的最大c 也就是找到右边界
                while left < right:
                    mid = left + (right - left + 1) // 2
                    if nums[mid] >= cur_sum:  # 注意这里  反面
                        right = mid - 1
                    else:
                        left = mid
                res += (left - j)   # left - (j+1) + 1 = left - j
        return res

