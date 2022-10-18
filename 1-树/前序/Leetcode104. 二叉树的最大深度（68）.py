"""
@Author: HuKai
@Date: 2022/6/0  10:43
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        max_depth = 0
        def dfs(node, cur_depth):
            nonlocal max_depth
            if not node: return
            if not node.left and not node.right:
                max_depth = max(max_depth, cur_depth + 1)
            dfs(node.left, cur_depth + 1)
            dfs(node.right, cur_depth + 1)
        dfs(root, 0)
        return max_depth