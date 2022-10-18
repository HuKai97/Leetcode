class Solution:
    def translateNum(self, num: int) -> int:
        # https://www.bilibili.com/video/BV1Bz411i7cs?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        if not num: return 1
        num = str(num)
        # dp[i]表示num[:i]有多少种翻译方式
        # dp[5] num[:5] = 12258有多少种翻译方式
        dp = [0 for _ in range(len(num)+1)]
        dp[0] = 1   # dp[0]表示nums[:0]空串  1种
        dp[1] = 1   # dp[1]表示nums[:1]  1   1种
        for i in range(2, len(num)+1):
            # i=4时  num[i-2:i] = num[2:4] = 25
            if '10' <= num[i-2:i] <= '25':
                dp[i] = dp[i-1] + dp[i-2]
            # i=5时  num[i-2:i] = num[3:5] = 58
            else:
                dp[i] = dp[i-1]
        return dp[-1]