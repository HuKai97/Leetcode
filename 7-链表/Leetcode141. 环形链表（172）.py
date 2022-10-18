"""
@Author: HuKai
@Date: 2022/5/26  8:49
@github: https://github.com/HuKai97
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:  # 注意这里还有个fast.next条件
            slow = slow.next
            fast = fast.next.next
            if slow == fast: return True  # 相等就相遇了
        return False