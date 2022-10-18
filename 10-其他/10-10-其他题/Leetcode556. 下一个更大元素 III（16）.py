class Solution:
    def nextGreaterElement(self, n: int) -> int:
        res = []
        while n:
            res.append(n % 10)
            n //= 10
        res = res[::-1]

        # 找到第一个升序的位置 i
        i = len(res) - 2
        while i >= 0 and res[i+1] <= res[i]: i -= 1

        # 找到第一个比res[i]更大的数 j
        if i >= 0:
            j = len(res) - 1
            while j > i and res[j] <= res[i]: j -= 1
            res[i], res[j] = res[j], res[i]
        else: return -1

        # 排序
        start, end = i + 1, len(res) - 1
        while start < end:
            res[start], res[end] = res[end], res[start]
            start += 1
            end -= 1
        ans = 0
        while res:
            ans = ans * 10 + res.pop(0)
        return ans if ans <= 2**31 - 1 else -1