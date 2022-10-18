# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # https://www.bilibili.com/video/BV1LS4y1R7T8?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        # 返回删除节点key后的root为根节点的二叉搜索树
        if not root: return None
        # 寻找要删除的节点 -> 删除左子树中节点
        if root.val > key: root.left = self.deleteNode(root.left, key)
        # 寻找要删除的节点 -> 删除右子树中节点
        elif root.val < key: root.right = self.deleteNode(root.right, key)
        else:
            # 已经找到要删除的节点
            # 如果当前要删除的节点是叶子节点
            if not root.left and not root.right: return None
            # 如果左子树为空 右子树不为空
            elif not root.left and root.right: return root.right
            # 如果左子树不为空 右子树为空
            elif root.left and not root.right: return root.left
            else:
                # 左右子树都不为空
                temp = root.right
                while temp and temp.left:
                    temp = temp.left
                root.val, temp.val = temp.val, root.val
                root.right = self.deleteNode(root.right, key)
        return root