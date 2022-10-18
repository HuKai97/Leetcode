"""
@Author: HuKai
@Date: 2022/5/28  9:21
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.res = float('-inf')
        def dfs(root):
            if not root: return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            self.res = max(self.res, left + right + root.val)
            return max(left, right) + root.val
        dfs(root)
        return self.res