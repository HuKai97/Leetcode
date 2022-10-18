"""
@Author: HuKai
@Date: 2022/5/31  23:12
@github: https://github.com/HuKai97
"""
# 比较难的一道题
# bili: https://www.bilibili.com/video/BV1z54y1b7wb?spm_id_from=333.337.search-card.all.click
# leetcode讲解: https://leetcode.cn/problems/median-of-two-sorted-arrays/solution/xiang-xi-tong-su-de-si-lu-fen-xi-duo-jie-fa-by-w-2/
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 对两个数组同时用二分法  中位数=特殊的找两个数组第k小的元素
        # 每次一半一半的删除，找第k小，那我一次就可以排除掉k/2的元素
        def getKth(start1, end1, start2, end2, k):
            len1, len2 = end1-start1+1, end2-start2+1
            if len1 == 0: return nums2[start2+k-1]
            if len2 == 0: return nums1[start1+k-1]
            if k == 1: return min(nums1[start1], nums2[start2])
            i, j = start1 + min(len1, k//2) - 1, start2 + min(len2, k//2) - 1
            if nums1[i] > nums2[j]:
                return getKth(start1, end1, j+1, end2, k-(j-start2+1))
            else:
                return getKth(i+1, end1, start2, end2, k-(i-start1+1))
        m, n = len(nums1), len(nums2)
        left, right = (m+n+1)//2, (m+n+2)//2
        # 将偶数和奇数的情况合并，如果是奇数，会求两次同样的 k
        return (getKth(0, m-1, 0, n-1, left) + getKth(0, m-1, 0, n-1, right)) / 2