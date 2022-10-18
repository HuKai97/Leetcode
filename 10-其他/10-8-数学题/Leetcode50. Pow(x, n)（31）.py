class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n == 1: return x
        def pow(x, cur):
            if cur == 0: return 1
            y = pow(x, cur // 2)
            return y * y if cur % 2 == 0 else y * y * x
        return pow(x, n) if n >= 0 else 1.0 / pow(x, -n)