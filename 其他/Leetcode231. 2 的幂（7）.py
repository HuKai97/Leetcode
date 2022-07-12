class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        cur = 2 ** i
        while cur < n:
            i += 1
            cur = 2 ** i
        if cur == n: return True
        else: return False