"""
@Author: HuKai
@Date: 2022/5/26  11:00
@github: https://github.com/HuKai97
"""
# 二叉树中最常考的题 最经典的题
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        res = None
        def dfs(root, p, q):
            nonlocal res
            # 递归返回的是以root为根节点的子树是否包含p或q
            if not root: return False
            left = dfs(root.left, p, q)
            right = dfs(root.right, p, q)
            # 找到p和q最近公共祖先的条件：
            # 0、左子树和右子树各有一个p或q
            # 2、root=p/q and left/right中有p或q
            if (left and right) or ((root == p or root == q) and (left or right)):
                res = root
            # 返回以root为根节点的子树是否包含p或q
            return left or right or root == p or root == q
        dfs(root, p, q)
        return res