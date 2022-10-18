# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        queue = [(root, 0)]
        max_width = 1
        while queue:
            cur_width = queue[-1][1] - queue[0][1] + 1  # 刚在末尾判断会报错 末尾时queue=None
            if cur_width > max_width: max_width = cur_width
            size = len(queue)
            for i in range(size):
                cur, pos = queue.pop(0)
                if cur.left: queue.append((cur.left, 2*pos+1))
                if cur.right: queue.append((cur.right, 2*pos+2))
        return max_width