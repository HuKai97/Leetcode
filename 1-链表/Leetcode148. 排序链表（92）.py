"""
@Author: HuKai
@Date: 2022/6/1  10:13
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def merge(self, head1, head2):
        dummy = ListNode(-1)
        rear = dummy
        p, q = head1, head2
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

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 归并排序
        if not head or not head.next: return head
        # 找到链表中点  奇数找到中点   偶数找到中点前面一个数
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 把链表切成两部分，再对这俩个部分进行排序
        head2 = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(head2)
        return self.merge(left, right)