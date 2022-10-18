class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # https://www.bilibili.com/video/BV1RL411P7WQ?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        m, n, t = len(s1), len(s2), len(s3)
        if m + n != t: return False
        # dp[i][j] 表示s1[:i]和s2[:j]是否能交错组成s3[:i+j]
        dp = [[False for _ in range(n+1)]for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            # s1[:i] 能否拼成 s3[:i]
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            # s2[:j] 能否拼成 s3[:j]
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        return dp[-1][-1]