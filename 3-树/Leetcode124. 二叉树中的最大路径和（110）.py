"""
@Author: HuKai
@Date: 2022/5/28  9:21
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_path_sum = float('-inf')
        def dfs(root):
            nonlocal max_path_sum
            if not root: return 0
            left, right = max(dfs(root.left), 0), max(dfs(root.right), 0)
            max_path_sum = max(max_path_sum, left+right+root.val)
            return max(left, right) + root.val
        dfs(root)
        return max_path_sum