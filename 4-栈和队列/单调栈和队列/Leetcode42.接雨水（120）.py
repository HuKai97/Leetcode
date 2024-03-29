"""
@Author: HuKai
@Date: 2022/5/31  20:59
@github: https://github.com/HuKai97
"""
# https://www.bilibili.com/video/BV1fi4y1t7BP?spm_id_from=333.337.search-card.all.click
class Solution:
    def trap(self, height: List[int]) -> int:
        # 单调递减栈  存储柱子的下标
        # 每个位置接到的最多雨水=(min(左侧第一个大于，右侧第一个大于)-当前位置的高度) * 宽度
        if len(height) < 2: return 0
        stack = []
        res = 0
        for i in range(len(height)):
            # 找到右侧第一个比当前元素大的  左边第一个比当前元素大的刚好在单调栈栈顶
            while stack and height[i] > height[stack[-1]]:
                # 说明积水可以在stack[-2]->i之间形成
                cur_height = height[stack.pop()]  # 当前元素的高度    0
                if not stack: break
                h = min(height[i], height[stack[-1]]) - cur_height  # min 木桶原理   min(0,2)-0=0
                w = i - stack[-1] - 1  # 2-0-0=0
                res += (h * w)  # 0+=0*0=0
            stack.append(i)
        return res