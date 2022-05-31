"""
@Author: HuKai
@Date: 2022/5/28  9:39
@github: https://github.com/HuKai97
"""
import heapq
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: return
        if len(lists) == 1: return lists[0]
        dummy = ListNode(-1)
        rear = dummy
        hp = []
        for idx in range(len(lists)):
            if lists[idx]:
                heapq.heappush(hp, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        while hp:
            val, idx = heapq.heappop(hp)
            rear.next = ListNode(val)
            rear = rear.next
            if lists[idx]:
                heapq.heappush(hp, (lists[idx].val, idx))
                lists[idx] = lists[idx].next
        return dummy.next