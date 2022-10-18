# https://www.bilibili.com/video/BV1ib4y1h7bv?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [[0]]
        res = [[] for _ in range(n+1)]
        res[0] = ['0']
        for i in range(1, n+1):
            reverse = res[i-1][::-1]
            res[i] = res[i-1] + reverse
            for j in range(len(res[i-1])):
                res[i][j] += '0'
            for j in range(len(res[i-1]), 2*len(res[i-1])):
                res[i][j] += '1'
        for i in range(len(res[n])):
            res[n][i] = int(res[n][i], 2)
        return res[n]