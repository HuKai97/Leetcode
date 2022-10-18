"""
@Author: HuKai
@Date: 2022/5/26  8:55
@github: https://github.com/HuKai97
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = [root]
        reverse = False  # 当前层是否逆序
        res = []
        while queue:
            size, arr = len(queue), []
            for i in range(size):
                cur_node = queue.pop(0)
                arr.append(cur_node.val)
                if cur_node.left: queue.append(cur_node.left)
                if cur_node.right: queue.append(cur_node.right)
            if reverse == True:
                res.append(arr[::-1])
                reverse = False
            else:
                res.append(arr)
                reverse = True
        return res
