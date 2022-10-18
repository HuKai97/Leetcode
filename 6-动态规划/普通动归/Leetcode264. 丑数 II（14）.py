class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # https://www.bilibili.com/video/BV19m4y1D7Za?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        if n == 1: return 1
        dp = [0] * n
        dp[0] = 1
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[p2]*2, dp[p3]*3, dp[p5]*5)
            if dp[i] == dp[p2]*2: p2 += 1
            if dp[i] == dp[p3]*3: p3 += 1
            if dp[i] == dp[p5]*5: p5 += 1
        return dp[n-1]