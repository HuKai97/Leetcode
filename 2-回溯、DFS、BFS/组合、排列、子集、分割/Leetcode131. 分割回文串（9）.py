class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True
        def dfs(start, path, res):
            if start == len(s):
                res.append(copy.deepcopy(path))
                return

            for i in range(start, len(s)):
                if check(s[start: i+1]):
                    path.append(s[start: i+1])
                    dfs(i+1, path, res)
                    path.pop()
        start = 0
        path, res = [], []
        dfs(start, path, res)
        return res