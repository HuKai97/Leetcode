"""
@Author: HuKai
@Date: 2022/5/25  9:53
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        dummy = ListNode(-1)
        rear = dummy
        p, q = list1, list2
        while p and q:
            if p.val <= q.val:
                rear.next = p
                p = p.next
            else:
                rear.next = q
                q = q.next
            rear = rear.next
        rear.next = p if p else q
        return dummy.next