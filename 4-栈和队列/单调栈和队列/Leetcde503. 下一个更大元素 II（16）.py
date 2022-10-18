class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # https://www.bilibili.com/video/BV1oh411m7yy?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        stack = []
        n = len(nums)
        res = [-1] * n
        for i in range(n * 2):  # 循环数组  需要遍历一个来回
            num = nums[i % n]   # 需要遍历一个来回
            while stack and num > nums[stack[-1]]:
                top = stack.pop()
                res[top] = num
            if i < n:  # 只需要压入整个数组即可  不需要重复压入
                stack.append(i)
        return res