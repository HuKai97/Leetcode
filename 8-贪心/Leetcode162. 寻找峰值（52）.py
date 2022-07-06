class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) < 2: return 0
        res = []  # 存放所有极大值
        # 找极大值  pre>0  cur<0
        pre, cur = 0, 0
        for i in range(1, len(nums)):
            cur = nums[i] - nums[i-1]
            if i == 1 and cur < 0: res.append(0)  # 判断第一个元素是不是极大值
            if cur < 0 and pre > 0:  # 找到[1~n-1]所有的极大值
                res.append(i-1)
            # if cur > 0 and pre < 0:  # 找到[1~n-1]所有的极小值
            #     res.append(i-1)
            pre = cur
        if cur > 0: res.append(len(nums) - 1)  # 判断最后一个元素是不是极大值
        return res[0]

        # 二、二分查找  O(log(n))
        # 这道题之所以可以用二分 主要是因为nms[-1] = nums[n] = -∞
        # 视频讲解：https://www.bilibili.com/video/BV1BU4y1T7ri?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        if len(nums) < 2: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid
        return left