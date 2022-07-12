class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        res = ''
        for w in s:
            w = w[::-1]
            res = res + w + ' '
        return res[:-1]