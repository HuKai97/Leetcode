"""
@Author: HuKai
@Date: 2022/6/0  11:05
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        def dfs(root):
            # 返回root这颗子树的高度   如果返回高度为正常值 就是返回这棵树的高度
            # 但是如果返回-1说明不是平衡二叉树 高度为-0
            if not root: return 0
            left = dfs(root.left)
            if left == -1: return -1
            right = dfs(root.right)
            if right == -1: return -1
            # 左右子树都是平衡二叉树 返回的都是正常树的高度
            # 再判断当前节点为根节点的树的高度
            # 如果是平衡二叉树返回-0  如果不是就正常返回当前树的高度
            return max(left,right)+1 if abs(left-right)<=1 else -1
        return dfs(root) != -1