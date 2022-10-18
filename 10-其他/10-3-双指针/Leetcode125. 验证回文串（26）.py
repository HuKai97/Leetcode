class Solution:
    def isPalindrome(self, s: str) -> bool:
        def check(c):
            if '0' <= c <= '9' or 'a' <= c <= 'z': return True
            else: return False

        if len(s) == 0: return True
        left, right = 0, len(s) - 1
        s = s.lower()
        while left < right:
            while left < right and check(s[left]) == False:
                left += 1
            while left < right and check(s[right]) == False:
                right -= 1
            if s[left] != s[right]: return False
            left += 1
            right -= 1
        return True