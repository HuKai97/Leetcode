# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # 0、递归
        self.res = []
        def dfs(root):
            if not root: return
            dfs(root.left)
            dfs(root.right)
            self.res.append(root.val)
        dfs(root)
        return self.res

        # 2、迭代
        # 后序：左右根  前序：根左右
        res = []
        stack, cur = [], root
        while cur or stack:
            while cur:
                res.append(cur.val)
                stack.append(cur)
                cur = cur.right
            cur = stack.pop()
            cur = cur.left
        return res[::-1]