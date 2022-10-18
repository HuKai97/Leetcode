class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def get_heights(cur_row, heights):
            # cur_arr：matrix中当前层的0、1值
            # 根据上一层的heights求当前层的heights
            for i in range(len(cur_row)):
                if cur_row[i] == '0': heights[i] = 0
                else: heights[i] += 1
            return heights

        def largestArea(heights):
            # 求柱状图中最大的矩形 和84一模一样
            stack = []
            res = 0
            heights = [0] + heights + [0]
            for i in range(len(heights)):
                while stack and heights[i] < heights[stack[-1]]:
                    cur_h = heights[stack.pop()]
                    cur_w = i - stack[-1] - 1
                    res = max(res, cur_h * cur_w)
                stack.append(i)
            return res

        if not matrix: return 0
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            if i == 0:  heights = [int(x) for x in matrix[0]]
            else: heights = get_heights(matrix[i], heights)
        # print(heights)
            cur_row_max_area = largestArea(heights)
            res = max(res, cur_row_max_area)
        return res
