class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        print(intervals)  # [[1, 2], [1, 3], [2, 3], [3, 4]]
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:  # 出现重叠区间
                res += 1                             # 结果 +1
                # intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                # 删除一个区间，删除有边界更大的那个区间 留下右边界更小的区间  可以让移除的区间数最小
                intervals[i][1] = min(intervals[i-1][1], intervals[i][1])
        return res