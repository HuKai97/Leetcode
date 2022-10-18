# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        def robTree(root):
            if not root: return [0, 0]
            left = robTree(root.left)
            right = robTree(root.right)

            # 不偷root
            val1 = max(left) + max(right)
            # 偷root
            val2 = root.val + left[0] + right[0]

            return [val1, val2]

        return max(robTree(root))