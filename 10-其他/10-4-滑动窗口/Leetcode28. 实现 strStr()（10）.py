class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        for end in range(len(needle)-1, len(haystack)):
            if haystack[start: end+1] == needle:
                return start
            start += 1
        return -1