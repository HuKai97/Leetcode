import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # https://leetcode.cn/problems/meeting-rooms-ii/solution/hui-yi-shi-ii-jian-dan-tan-xin-you-xian-x7kuo/
        intervals.sort(key = lambda x: x[0])
        end_hp = [intervals[0][1]]  # 记录所有正在开的会议室的结束时间
        res = 1
        for i in range(1, len(intervals)):
            # 当前会议的开始时间比之前所有已开会议的最早结束时间还要早，需增加会议室
            if intervals[i][0] < end_hp[0]:
                res += 1
                heapq.heappush(end_hp, intervals[i][1])
            # 可以在最早结束的会议之后开始当前会议，之前的最早结束时间变成当前会议结束的时间
            else:
                heapq.heappop(end_hp)
                heapq.heappush(end_hp, intervals[i][1])
        return res



# 252. 会议室
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x : x[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]: return False
        return True