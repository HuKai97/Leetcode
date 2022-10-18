class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        mapp = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def dfs(idx, path, res):
            if idx == len(digits):
                res.append(path)
                return
            cur_letters = mapp[str(digits[idx])]
            for letter in cur_letters:
                path += letter
                dfs(idx+1, path, res)
                path = path[:-1]

        cur_idx = 0
        res = []
        path = ''
        dfs(cur_idx, path, res)
        return res