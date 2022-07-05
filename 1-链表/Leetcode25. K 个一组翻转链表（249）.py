"""
@Author: HuKai
@Date: 2022/5/26  18:42
@github: https://github.com/HuKai97
"""
# hard题
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, start, end):
        # 把start->end-1位置的节点逆序
        # return是的end-1 -> start
        pre, cur = None, start
        while cur != end:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        return pre
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        dummy = ListNode(-1)
        rear = dummy
        k_start, k_end = head, head
        while k_end:
            for i in range(k):
                if not k_end:
                    rear.next = k_start
                    return dummy.next
                k_end = k_end.next
            # return的是k_end-1 -> k_start    再下面的节点就是k_end(还没翻转)
            # k_end-1 -> k_start（翻转后）   k_end（还没翻转）
            rear.next = self.reverse(k_start, k_end)
            rear = k_start
            k_start = k_end
        return dummy.next