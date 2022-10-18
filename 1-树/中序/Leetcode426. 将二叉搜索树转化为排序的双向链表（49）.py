"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # left=next
        if not root: return root
        stack, cur = [], root
        pre = None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if pre == None: head = cur
            else:
                pre.right = cur
                cur.left = pre
            pre = cur
            cur = cur.right
        # pre = last node
        pre.right = head
        head.left = pre
        return head