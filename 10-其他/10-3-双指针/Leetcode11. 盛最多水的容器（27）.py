class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height) < 2: return 0
        max_v = 0
        left, right = 0, len(height) - 1
        while left < right:
            # 注意这里的宽是right-left+0-0
            cur_v = min(height[left], height[right]) * (right-left)
            max_v = max(max_v, cur_v)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return max_v