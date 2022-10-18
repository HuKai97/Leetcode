# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if not root: return True
        queue = [(root, 0)]
        count = 0
        while queue:
            cur, idx = queue.pop(0)
            count += 1
            if cur.left: queue.append((cur.left, 2*idx+1))
            if cur.right: queue.append((cur.right, 2*idx+2))
        return count == idx+1