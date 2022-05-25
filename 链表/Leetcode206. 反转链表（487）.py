"""
@Author: HuKai
@Date: 2022/5/25  8:32
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # 头插法
        dummy = ListNode(-1)
        p = head
        while p:
            temp = p.next
            p.next = dummy.next
            dummy.next = p
            p = temp
        return dummy.next