class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # https://www.bilibili.com/video/BV1BA411T7SU?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        if not triangle: return 0
        m = len(triangle)
        # dp[i][j]表示从bittim->triangle[i][j]的最小路径和
        dp = triangle
        # base case: 初始化最下面一行 就等于triangle[-1][j]
        # 从倒数第二行开始遍历
        for i in range(m-2, -1, -1):
            for j in range(len(triangle[i])):
                # 如果从上开始遍历 dp[i][j] = min(dp[i-1][j], dp[i-1][j+1]) + tri[i][j]
                # 可能上一层完全就不存在dp[i-1][j+1] 所以这里为了方便直接从底开始
                dp[i][j] += min(dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]