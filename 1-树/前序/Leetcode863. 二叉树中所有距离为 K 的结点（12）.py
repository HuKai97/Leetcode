# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        # https://leetcode.cn/problems/all-nodes-distance-k-in-binary-tree/solution/er-cha-shu-zhong-suo-you-ju-chi-wei-kde-nlct0/
        if not root: return []
        self.res = []
        mapp = dict()  # key: child   val: parent

        def dfs_get_parent(node):
            # 找到所有节点的父亲节点  方便向上遍历
            if not node: return
            if node.left:
                mapp[node.left] = node
            if node.right:
                mapp[node.right] = node
            dfs_get_parent(node.left)
            dfs_get_parent(node.right)

        def dfs_find_res(cur, pre, idx):
            if not cur: return
            if idx == k:
                self.res.append(cur.val)
                return
                # 如果是只向下找 是不可能出现重复元素的  但是这里会向上找 所以可能会重复 需要设置一定条件
            # 所以每走一个节点都要确定一下当前节点肯定不等于上一时刻刚走了的节点  不能走回头路
            # 往左走  需要肯定左子树不等于上一个节点   如 535
            if cur.left != pre:
                dfs_find_res(cur.left, cur, idx + 1)
            # 往右走  需要肯定右子树不等于上一个节点   如 252
            if cur.right != pre:
                dfs_find_res(cur.right, cur, idx + 1)
            # 往上走  需要肯定有父亲节点 且 父亲节点不等于上一个节点  如 353
            if cur in mapp and mapp[cur] != pre:
                dfs_find_res(mapp[cur], cur, idx + 1)

        dfs_get_parent(root)
        dfs_find_res(target, None, 0)
        return self.res
