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
            # node.left, node.right = node.right, node.left
            dfs(node.left)
            dfs(node.right)
            node.left, node.right = node.right, node.left
        dfs(root)
        return root