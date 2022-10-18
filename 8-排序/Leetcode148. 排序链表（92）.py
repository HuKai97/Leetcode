"""
@Author: HuKai
@Date: 2022/6/0  10:13
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(head1, head2):
            dummy = ListNode(-1)
            rear = dummy
            p, q = head1, head2
            while p and q:
                if p.val < q.val:
                    rear.next = p
                    rear = rear.next
                    p = p.next
                else:
                    rear.next = q
                    rear = rear.next
                    q = q.next
            rear.next = p if p else q
            return dummy.next
        def merge_sort(head):
            if not head or not head.next: return head
            dummy = ListNode(-1, head)
            slow, fast = dummy, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            head2 = slow.next
            slow.next = None
            left, right = merge_sort(head), merge_sort(head2)
            return merge(left, right)
        return merge_sort(head)