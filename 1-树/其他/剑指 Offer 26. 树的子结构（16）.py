# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def is_contain(A, B):
            # A是否包含B
            if not B: return True
            if not A: return False
            if A.val != B.val: return False
            else: return is_contain(A.left, B.left) and is_contain(A.right, B.right)

        if not A or not B: return False
        if is_contain(A, B): return True
        else: return self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)