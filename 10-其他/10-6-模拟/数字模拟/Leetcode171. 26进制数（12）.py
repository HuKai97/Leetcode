class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for c in columnTitle:
            num = ord(c) - ord('A') + 1
            res = res * 26 + num
        return res