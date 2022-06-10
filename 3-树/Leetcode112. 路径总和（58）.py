# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        self.flag = False
        def dfs(root, cur_sum):
            if not root: return
            if not root.left and not root.right:
                if cur_sum - root.val == 0:
                    self.flag = True
            dfs(root.left, cur_sum-root.val)
            dfs(root.right, cur_sum-root.val)
        dfs(root, targetSum)
        return self.flag