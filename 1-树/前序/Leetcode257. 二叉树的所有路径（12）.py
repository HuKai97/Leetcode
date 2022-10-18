# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # pathStr += root.val + '->'
        def dfs(root, path, res):
            if not root: return
            if not root.left and not root.right:
                path += str(root.val)
                res.append(path)
                return
            dfs(root.left, path + str(root.val) + '->', res)
            dfs(root.right, path + str(root.val) + '->', res)

        if not root: return []
        if not root.left and not root.right: return [str(root.val)]
        path, res = '', []
        dfs(root, path, res)
        return res