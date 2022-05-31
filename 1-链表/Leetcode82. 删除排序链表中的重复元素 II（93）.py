"""
@Author: HuKai
@Date: 2022/5/28  9:01
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        pre, cur = dummy, head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.val == cur.next.val:
                    cur = cur.next
                    if not cur.next: break
                pre.next = cur.next
                cur = pre.next
            else: pre, cur = pre.next, cur.next
        return dummy.next