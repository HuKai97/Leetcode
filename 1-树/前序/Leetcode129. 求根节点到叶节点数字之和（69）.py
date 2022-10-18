"""
@Author: HuKai
@Date: 2022/6/0  10:39
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        res = 0
        def dfs(node, path_sum):
            nonlocal res
            if not node: return
            if not node.left and not node.right:
                res += path_sum * 10 + node.val
                return
            dfs(node.left, path_sum*10+node.val)
            dfs(node.right, path_sum*10+node.val)
        dfs(root, 0)
        return res