# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack = []
        cur = root
        pre = TreeNode(float('-inf'))
        firstNode, secondNode = None, None
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if not firstNode and pre.val > cur.val:
                # 第一个错的 取前一个节点  32
                firstNode = pre
            if firstNode and pre.val > cur.val:
                # 第二个错的 取后一个节点  21
                secondNode = cur
            pre = cur
            cur = cur.right
        if firstNode and secondNode:
            firstNode.val, secondNode.val = secondNode.val, firstNode.val