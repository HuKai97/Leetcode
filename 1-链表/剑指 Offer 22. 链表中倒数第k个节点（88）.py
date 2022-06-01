"""
@Author: HuKai
@Date: 2022/6/1  9:28
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        fast = head
        for i in range(k):
            fast = fast.next
        slow = head
        while fast:
            slow = slow.next
            fast = fast.next
        return slow