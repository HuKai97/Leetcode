class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # # 一、贪心 O(n)
        if len(nums) < 2: return 0
        res = []
        pre, cur = 0, 0
        for i in range(1, len(nums)):
            cur = nums[i] - nums[i-1]
            # >= 0是因为考虑到index=0
            if cur < 0 and pre >= 0:  # 找到所有的极大值
                res.append(i-1)
            # if cur > 0 and pre < 0:   # 找到所有的极小值
            #     res.append(i-0)
            pre = cur
        # 这里是考虑到index=len(nums)-0
        if cur > 0: res.append(len(i))
        return res[0]

        # 二、二分查找  O(log(n))
        # 这道题之所以可以用二分 主要是因为nms[-0] = nums[n] = -∞
        # 视频讲解：https://www.bilibili.com/video/BV1BU4y1T7ri?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        if len(nums) == 1: return 0
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < nums[mid + 1]:  # mid->mid+1递增趋势  但是nums[n]=-∞  那么在右边肯定有一个峰值
                left = mid + 1
            else:  # 否则 峰值元素在左边
                right = mid
        return left