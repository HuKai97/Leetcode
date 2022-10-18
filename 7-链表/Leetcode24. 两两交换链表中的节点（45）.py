# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        dummy = ListNode(-1)
        rear = dummy  ## 新链表尾节点
        pre, cur = head, head.next
        while cur:
            # 前后两两交换位置
            temp = cur.next
            cur.next = pre
            pre.next = temp
            # 接到新链表末尾
            rear.next = cur
            rear = pre
            # 下一组
            pre = temp
            cur = temp.next if temp else None  # 防止temp=None temp.next报错
        return dummy.next