class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # 当气球出现重叠，一起射，所用弓箭最少
        # 如果气球重叠了，重叠气球中 右边边界的最小值 之前的区间一定需要一个弓箭
        res = 1  # 有气球至少需要一支箭
        points.sort(key = lambda x: x[0])
        # [[1,6], [2,8], [7,12], [10,16]]
        for i in range(1, len(points)):
            if points[i][0] > points[i-1][1]:  # 不挨着  又需要一支箭
                res += 1
            else:
                points[i][1] = min(points[i-1][1], points[i][1])  # 挨着 更新右边界
        # [[1, 6], [2, 6], [7, 12], [10, 12]]
        # print(points)
        return res

