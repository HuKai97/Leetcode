"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # 复制链表中的指针都不应指向原链表中的节点 。
        if not head: return None
        mapp = {}
        # 先遍历一遍 复制节点 和 节点值
        cur = head
        while cur:
            mapp[cur] = Node(cur.val)
            cur = cur.next
        # 再遍历一遍
        cur = head
        while cur:
            if cur.next: mapp[cur].next = mapp[cur.next]
            if cur.random: mapp[cur].random = mapp[cur.random]
            cur = cur.next
        return mapp[head]