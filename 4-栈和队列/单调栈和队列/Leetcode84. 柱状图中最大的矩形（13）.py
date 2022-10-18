class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # https://www.bilibili.com/video/BV1fi4y1d7YX?spm_id_from=333.999.0.0&vd_source=5f6bbc1038b075757cb446f800f3cd56
        if not heights: return 0
        if len(heights) == 1: return heights[0]
        stack = []
        heights = [0] + heights + [0]
        res = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                cur_h = heights[stack.pop()]
                cur_w = i - stack[-1] - 1
                res = max(res, cur_h * cur_w)
            stack.append(i)
        return res