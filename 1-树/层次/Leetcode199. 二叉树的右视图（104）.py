"""
@Author: HuKai
@Date: 2022/5/27  11:26
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # 层次遍历
        if not root: return []
        res, queue = [], [root]
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.pop(0)
                if i == size-1:
                    res.append(cur.val)
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
        return res