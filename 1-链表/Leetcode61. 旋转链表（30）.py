# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0: return head
        cur = head
        length = 0
        while cur:
            cur = cur.next
            length += 1
        k %= length
        if k == 0: return head

        dummy = ListNode(-1, head)
        slow, fast = head, head
        pre = dummy
        for i in range(k):
            fast = fast.next
        while fast.next:
            pre = pre.next
            slow = slow.next
            fast = fast.next
        head2 = slow.next
        slow.next = None
        head2_tail = fast
        head2_tail.next = dummy.next
        dummy.next = head2
        return dummy.next