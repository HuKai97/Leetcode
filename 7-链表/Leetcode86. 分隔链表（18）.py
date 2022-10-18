# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy1, dummy2 = ListNode(-1), ListNode(-2)
        rear1, rear2 = dummy1, dummy2
        p = head
        while p:
            temp = p.next
            if p.val < x:
                rear1.next = p
                rear1 = rear1.next
                rear1.next = None
            else:
                rear2.next = p
                rear2 = rear2.next
                rear2.next = None
            p = temp
        rear1.next = dummy2.next
        return dummy1.next