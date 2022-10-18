"""
@Author: HuKai
@Date: 2022/5/27  10:04
@github: https://github.com/HuKai97
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        m, n = len(matrix), len(matrix[0])
        left, right, top, bottom = 0, n - 1, 0, m - 1
        count = 0
        res = []
        while count < m * n:
            # 向右走
            for j in range(left, right+1):
                # 注意这里要加上这个判断条件 否则[[0,2,3,4],[5,6,7,8],[9,10,11,12]]
                # 会错：[0,2,3,4,8,12,11,10,9,5,6,7,6]
                if count < m * n:
                    res.append(matrix[top][j])
                    count += 1
            top += 1
            # 往下走
            for i in range(top, bottom+1):
                if count < m * n:
                    res.append(matrix[i][right])
                    count += 1
            right -= 1
            # 往左走
            for j in range(right, left-1, -1):
                if count < m * n:
                    res.append(matrix[bottom][j])
                    count += 1
            bottom -= 1
            # 往上走
            for i in range(bottom, top-1, -1):
                if count < m * n:
                    res.append(matrix[i][left])
                    count += 1
            left += 1
        return res

