# https://www.bilibili.com/video/BV1fg411d7E7?spm_id_from=333.337.search-card.all.click&vd_source=5f6bbc1038b075757cb446f800f3cd56
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 单调递减队列 queue 存储nums下标 队头存储当前窗口最大的值
        # 当nums[i]比queue的队尾元素还要大  就把queue中比nums[i]小的数全部pop出去
        # 再把i加进去 保证次数queue仍是单调递减的
        # 当i-q[0]>=k时,弹出队首元素 这个元素就是当前窗口的最大值
        queue = []
        res = []
        for i in range(len(nums)):
            # 队列不为空 且当前元素大于队尾元素 那就把queue中小于nums[i]的元素pop出来
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            # 把当前元素append进去 保证queue是一个单调递减的队列
            queue.append(i)
            # 判断窗口大小 队首元素还在不在窗口之内
            while queue and i - queue[0] + 1 > k:
                queue.pop(0)
            # 窗口没形成就只append进queue  但是还不append进res
            # i - 0 + 1 >= k
            if i + 1 >= k:
                res.append(nums[queue[0]])
        return res
