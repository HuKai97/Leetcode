"""
@Author: HuKai
@Date: 2022/5/27  11:01
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):
            pre, cur = None, head
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        if not head or not head.next: return head
        dummy = ListNode(-1)
        rear = dummy
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None
        head2 = reverse(head2)
        while head and head2:
            rear.next = head
            rear = rear.next
            head = head.next
            rear.next = head2
            rear = rear.next
            head2 = head2.next
        if head: rear.next = head
        return dummy.next