class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s: return 0
        g.sort()
        s.sort()
        res = 0
        idx = 0  # 胃口
        for i in range(len(s)):  # 对每个饼干  小饼干先喂饱小胃口
            if idx < len(g) and s[i] >= g[idx]:
                res += 1
                idx += 1
        return res