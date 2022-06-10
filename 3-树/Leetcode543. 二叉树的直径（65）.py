# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        self.max_count = 1
        def dfs(root):
            # 以root为根节点这颗树的最大深度
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # 记录以root为根节点这颗树的最大节点个数
            # root这颗树的最大节点个数=左子树最大节点个数+右子树最大节点个数+1
            self.max_count = max(self.max_count, left+right+1)
            return max(left, right) + 1
        dfs(root)
        # 最大直径=最大节点个数-1
        return self.max_count - 1