class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # https://www.bilibili.com/video/BV1U34y1q7UN?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        if numRows == 1: return s
        rows = ['' for _ in range(numRows)]
        cur_row = 0
        down = False  # 当前方向向上
        for i in range(len(s)):
            rows[cur_row] += s[i]
            if cur_row == 0 or cur_row == numRows - 1: down = not down
            cur_row += 1 if down == True else -1
        return ''.join(rows)