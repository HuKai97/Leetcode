# https://www.bilibili.com/video/BV1LA41137us?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        def getNum(version, idx):
            res = 0
            while idx < len(version) and '0' <= version[idx] <= '9':
                res = res * 10 + int(version[idx])
                idx += 1
            return res, idx
        idx1, idx2 = 0, 0
        while idx1 < len(version1) or idx2 < len(version2):
            num1, idx1 = getNum(version1, idx1)
            num2, idx2 = getNum(version2, idx2)
            if num1 > num2: return 1
            if num1 < num2: return -1
            idx1 += 1  # 遇到.
            idx2 += 1
        return 0