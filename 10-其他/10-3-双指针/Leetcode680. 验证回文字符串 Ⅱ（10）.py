class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            left, right = 0, len(s) - 1
            while left < right:
                if s[left] != s[right]: return False
                left += 1
                right -= 1
            return True

        if len(s) < 2: return True
        if s == s[::-1]: return True
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1: right + 1]) or isPalindrome(s[left: right])