class Solution:
    def jump(self, nums: List[int]) -> int:
        # https://www.bilibili.com/video/BV1wL411p7Rx?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
        # 每一步都跳的最远 最终跳到最后一个位置所需的步长即为最小步长
        if len(nums) < 2: return 0
        steps = 0
        end = 0     # 这一步可以到达的最大位置
        maxPos = 0  # 下一步可以到达的最大位置
        # 到了len(nums) - 2的位置才有必要再跳  到了len(nums) - 1的位置是不需要再跳的
        for i in range(len(nums) - 1):
            maxPos = max(nums[i]+i, maxPos)
            if i == end:  # 走完了这个区间，往后跳一步，更新下一个区间
                end = maxPos
                steps += 1
        return steps