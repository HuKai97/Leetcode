# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.res = ''
        if not root: return self.res

        def dfs(root):
            if not root:
                self.res += ' #'
            else:
                self.res += ' ' + str(root.val)
                dfs(root.left)
                dfs(root.right)

        dfs(root)
        return self.res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data = list(data.split(' '))[1:]

        # print(data)
        def dfs():
            if data[0] == '#':
                data.pop(0)
                return None
            else:
                cur = TreeNode(data[0])
                data.pop(0)
                cur.left = dfs()
                cur.right = dfs()
                return cur

        return dfs()