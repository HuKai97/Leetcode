# Leetcode112. 路径总和
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        self.flag = False
        def dfs(root, cur):
            if not root: return
            if not root.left and not root.right:
                if cur - root.val == 0: self.flag = True
            dfs(root.left, cur-root.val)
            dfs(root.right, cur-root.val)
        dfs(root, targetSum)
        return self.flag

# Leetcode113. 路径总和 II
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        res = []
        path = []
        def dfs(root, cur, res, path):
            if not root: return
            if not root.left and not root.right:
                if cur - root.val == 0:
                    res.append(path+[root.val])
                    return
            dfs(root.left, cur-root.val, res, path+[root.val])
            dfs(root.right, cur-root.val, res, path+[root.val])
        dfs(root, targetSum, res, path)
        return res