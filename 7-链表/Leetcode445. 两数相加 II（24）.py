# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            pre, cur = None, head
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        l1, l2 = reverse(l1), reverse(l2)
        dummy = ListNode(-1, l1)
        rear = dummy
        p, q = l1, l2
        while p and q:
            p.val += q.val
            rear = rear.next
            p = p.next
            q = q.next
        if q: rear.next = q

        pre, cur = dummy.next, dummy.next.next
        while cur:
            cur.val += (pre.val // 10)
            pre.val %= 10
            pre = pre.next
            cur = cur.next
        if pre.val >= 10:
            pre.val %= 10
            pre.next = ListNode(1)
        return reverse(dummy.next)
