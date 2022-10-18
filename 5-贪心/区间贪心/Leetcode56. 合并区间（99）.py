"""
@Author: HuKai
@Date: 2022/5/28  10:51
@github: https://github.com/HuKai97
"""
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1: return intervals
        res = []
        intervals.sort(key = lambda x: x[0])  # 按第1位排序
        intervals.append([float('inf'), 0])   # 最后append一个区间 保证实际最后一个区间会append进res
        for i in range(1, len(intervals)):
            # 当前区间与前面区间重叠了 就把前面区间合并到当前区间  再比较下一个区间
            if intervals[i][0] <= intervals[i-1][1]:
                intervals[i][0] = min(intervals[i-1][0], intervals[i][0])
                intervals[i][1] = max(intervals[i-1][1], intervals[i][1])
            else:
                # 没有重叠 就把前一个区间append  因为当前区间还需要和后面区间对比
                # 最后一个区间和【float('inf'), 0】对比float('inf) 小于前一个区间的右部分
                # 所以最后一个区间也必会append进来
                res.append(intervals[i-1])
        return res