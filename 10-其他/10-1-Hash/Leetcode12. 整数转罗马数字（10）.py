class Solution:
    def intToRoman(self, num: int) -> str:
        #    0    1     2     3     4     5    6      7       8      9
        mapp = [
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],   # 个位
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],   # 十位
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],   # 百位
            ['', 'M', 'MM', 'MMM']                                          # 千位
        ]
        return mapp[3][num // 1000] + mapp[2][num % 1000 // 100] + mapp[1][num % 1000 % 100 // 10] + mapp[0][num % 1000 % 100 % 10]