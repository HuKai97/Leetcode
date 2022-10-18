# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# https://www.bilibili.com/video/BV1334y1y7qk?spm_id_from=333.337.search-card.all.click
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return None
        cur = root
        while cur:
            if cur.left:
                temp = cur.left
                while temp and temp.right:
                    temp = temp.right
                temp.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right