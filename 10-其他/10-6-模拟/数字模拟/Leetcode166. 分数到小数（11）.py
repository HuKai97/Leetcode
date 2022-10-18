class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0: return '0'
        res = []

        # 有负数
        if numerator * denominator < 0: res.append('-')
        numerator, denominator = abs(numerator), abs(denominator)

        res.append(str(numerator // denominator))
        remain = numerator % denominator
        # 整除
        if remain == 0: return ''.join(res)

        # 有小数
        mapp = {}  # remain: idx
        res.append('.')
        while remain != 0 and remain not in mapp:
            mapp[remain] = len(res)
            remain *= 10
            res.append(str(remain // denominator))
            remain %= denominator

        # 有循环
        if remain:
            insertIndex = mapp[remain]
            res.insert(insertIndex, '(')
            res.append(')')

        return ''.join(res)