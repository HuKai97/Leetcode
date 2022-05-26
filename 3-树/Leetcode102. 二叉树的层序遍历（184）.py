"""
@Author: HuKai
@Date: 2022/5/25  10:57
@github: https://github.com/HuKai97
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], [root]
        while queue:
            size, arr = len(queue), []
            for i in range(size):
                cur_node = queue.pop(0)
                arr.append(cur_node.val)
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
            res.append(copy.deepcopy(arr))
        return res