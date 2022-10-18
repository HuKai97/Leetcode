# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def isSameTree(tree1, tree2):
            # 判断两棵树是不是相同的树
            if not tree1 and not tree2: return True
            if not tree1 or not tree2: return False
            if tree1.val != tree2.val: return False
            else:
                return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)

        if not root and not subRoot: return True
        if not root or not subRoot: return False
        if isSameTree(root, subRoot) == True: return True
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)