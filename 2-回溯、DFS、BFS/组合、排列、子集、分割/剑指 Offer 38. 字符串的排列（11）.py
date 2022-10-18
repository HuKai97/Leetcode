class Solution:
    def permutation(self, s: str) -> List[str]:
        def dfs(path, used, res):
            if len(path) == len(s):
                res.add(path)
                return
            for i in range(len(s)):
                if used[i] == True: continue
                used[i] = True
                dfs(path+s[i], used, res)
                used[i] = False
        path = ''
        used = [False] * len(s)
        res = set()
        dfs(path, used, res)
        return list(res)