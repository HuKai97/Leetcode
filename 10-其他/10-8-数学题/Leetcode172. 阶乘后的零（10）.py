class Solution:
    def trailingZeroes(self, n: int) -> int:
        # https://www.bilibili.com/video/BV1u54y1b7Hs?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        # 统计所有元素的因子中5的个数
        res = 0
        while n >= 5:
            res += (n // 5)
            n //= 5
        return res