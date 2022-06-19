# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head: return True
        dummy = ListNode(-1)
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next  # 头插法将前半部分逆序
            slow.next = dummy.next
            dummy.next = slow
            slow = temp
        if fast: slow = slow.next
        p = dummy.next
        while p and slow:
            if p.val != slow.val: return False
            p = p.next
            slow = slow.next
        return True