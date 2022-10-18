# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            # 返回这棵树的节点个数
            if not root: return 0
            if not root.left and not root.right: return 1
            left_node, right_node = root, root
            left_h, right_h = 0, 0
            while left_node:
                left_node = left_node.left
                left_h += 1
            while right_node:
                right_node = right_node.right
                right_h += 1
            if left_h == right_h: return 2 ** left_h - 1
            else: return dfs(root.left) + dfs(root.right) + 1
        return dfs(root)