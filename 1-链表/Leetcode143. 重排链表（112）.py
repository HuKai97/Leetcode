"""
@Author: HuKai
@Date: 2022/5/27  11:01
@github: https://github.com/HuKai97
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(head):  # 尾插法
            pre, cur = None, head
            while cur:
                temp = cur.next
                cur.next = pre
                pre = cur
                cur = temp
            return pre
        if not head or not head.next: return head
        # 找中点 偶数[1,2,3,4] slow=234  奇数[1,2,3,4,5] slow=345
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        new_head = slow.next
        slow.next = None
        # print(head)  # 1 2 3
        new_head = reverse(new_head)  # 5 4
        # 交叉插入
        dummy = ListNode(-1)
        rear = dummy
        while head and new_head:
            rear.next = head
            head = head.next
            rear = rear.next

            rear.next = new_head
            new_head = new_head.next
            rear = rear.next
        # head 肯定必 new_head长
        if head: rear.next = head
        return dummy.next