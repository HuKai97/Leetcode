class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        i = 0
        cur = 2 ** i
        while cur < n:
            i += 1
            cur = 2 ** i
        return cur == n