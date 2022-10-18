"""
@Author: HuKai
@Date: 2022/5/27  11:09
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head or n == 0: return None
        dummy = ListNode(-1, head)
        slow, fast = dummy, head
        for i in range(n):
            fast =fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next