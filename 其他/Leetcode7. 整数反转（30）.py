class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x < 0:
            flag = -1
            x *= flag
        res = 0
        while x != 0:
            res = res * 10 + x % 10
            x //= 10
        res *= flag
        return res if -2**31 <= res <= 2**31-1 else 0