# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 前序后序都可以
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        def dfs(node):
            if not node: return
            left = dfs(node.left)
            right = dfs(node.right)
            node.left, node.right = right, left
        return dfs(root)


# 剑指 Offer 27. 二叉树的镜像
class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: return None
        def dfs(root):
            if not root: return
            left = dfs(root.left)
            right = dfs(root.right)
            root.left = right
            root.right = left
            return root
        return dfs(root)