"""
@Author: HuKai
@Date: 2022/5/27  10:34
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode(-1, head)
        pre = dummy
        last = head
        for _ in range(left-1):  # 找到left前面一个节点
            pre = pre.next
        for _ in range(right):   # 找到right后面一个节点
            last = last.next
        cur = pre.next
        pre.next = last
        for _ in range(right-left+1):  # 尾插法 逆序
            temp = cur.next
            cur.next = pre.next
            pre.next = cur
            cur = temp
        return dummy.next