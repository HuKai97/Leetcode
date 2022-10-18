class Solution:
    def compress(self, chars: List[str]) -> int:
        if len(chars) < 2: return len(chars)
        cur = 0  # 压缩后的字符串索引位置  逐区间压缩
        i = 0    # 当前区间的起始位置索引
        while i < len(chars):
            j = i  # 当前区间结束位置索引
            while j < len(chars) - 1 and chars[j] == chars[j+1]: j += 1
            chars[cur] = chars[i]
            cur += 1
            if j != i:
                times = str(j-i+1)
                for k in range(len(times)):
                    chars[cur] = times[k]
                    cur += 1
            i = j + 1  # 更新下一个区间的起始位置
        return cur