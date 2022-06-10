# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        queue = [root]
        while queue:
            n, arr = len(queue), []
            for _ in range(n):
                cur = queue.pop(0)
                if cur: arr.append(cur.val)
                else: arr.append('#')
                if cur:
                    queue.append(cur.left)
                    queue.append(cur.right)
            if arr != arr[::-1]: return False
        return True