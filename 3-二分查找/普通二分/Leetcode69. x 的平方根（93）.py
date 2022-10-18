"""
@Author: HuKai
@Date: 2022/6/0  9:53
@github: https://github.com/HuKai97
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        # 找到小于等于x的平方根的最大值 找右边界
        if x < 2: return x
        left, right = 1, x//2+1
        while left < right:
            mid = left + (right - left + 1) // 2
            if mid ** 2 > x:
                right = mid - 1
            else: left = mid
        return left