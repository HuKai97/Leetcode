"""
@Author: HuKai
@Date: 2022/6/1  10:21
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 一、递归
        if not root: return []
        res = []
        def dfs(root):
            if not root: return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res

        # 二、迭代
        if not root: return []
        res = []
        stack, cur = [], root
        while stack or cur:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right
        return res