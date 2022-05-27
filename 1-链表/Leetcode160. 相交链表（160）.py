"""
@Author: HuKai
@Date: 2022/5/27  8:58
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 1、如果相交 那么在第一次两个都交换了head后会必相交 return相交节点
        # 2、如果不相交 那么在第一次两者都交换了head后会同时走到链表末尾 同时为None return None
        if not headA or not headB: return None
        p, q = headA, headB
        while p != q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p