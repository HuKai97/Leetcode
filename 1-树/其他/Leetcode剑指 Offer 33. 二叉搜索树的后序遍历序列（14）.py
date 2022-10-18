class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder: return True
        def dfs(i, j):
            if i >= j: return True
            idx = i
            while postorder[idx] < postorder[j]: idx += 1
            mid = idx
            while postorder[idx] > postorder[j]: idx += 1
            return idx == j and dfs(i, mid-1) and dfs(mid, j-1)
        return dfs(0, len(postorder)-1)