class Solution:
    def reverseWords(self, s: str) -> str:
        def reverseString(s):
            left, right = 0, len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s
        def reverseEachWord(s):
            left, right = 0, 0
            while left < len(s):
                while right < len(s) and s[right] != ' ': right += 1
                s[left: right] = reverseString(s[left: right])
                left = right + 1
                right = left
            return s
        res = reverseEachWord(list(s))
        return ''.join(res)