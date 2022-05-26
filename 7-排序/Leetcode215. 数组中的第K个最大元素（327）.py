"""
@Author: HuKai
@Date: 2022/5/25  8:49
@github: https://github.com/HuKai97
"""
# 堆排序
# 视频讲解：https://www.bilibili.com/video/av47196993?from=search&seid=4351042127032790802&rt=V%2FymTlOu4ow%2Fy4xxNWPUZ21pzQFbVqcJSjKcQx%2BMqj0%3D
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # 堆排序   求最大用小顶堆  求最小用大顶堆
        # 1、自己实现堆
        def heapify(tree, n, i):  # 对以tree[i]为根节点的子树进行堆排序
            c1, c2 = 2 * i + 1, 2 * i + 2
            min_idx = i
            if c1 < n and tree[c1] < tree[min_idx]:
                min_idx = c1
            if c2 < n and tree[c2] < tree[min_idx]:
                min_idx = c2
            if min_idx != i:
                tree[i], tree[min_idx] = tree[min_idx], tree[i]
                heapify(tree, n, min_idx)

        def build_heap(tree, n):  # 对整棵树进行建堆
            last_node = n - 1
            parent = (last_node - 1) // 2
            for i in range(parent, -1, -1):
                heapify(tree, n, i)

        hp = nums[:k]
        build_heap(hp, k)
        for i in range(k, len(nums)):
            if nums[i] > hp[0]:
                hp[0] = nums[i]
                heapify(hp, k, 0)
        return hp[0]

        # 2、掉包实现堆
        hp = nums[:k]
        heapq.heapify(hp)  # 建立最小堆
        for i in range(k, len(nums)):
            if nums[i] > hp[0]:
                heapq.heappop(hp)  # 弹出堆顶元素（最小值） 堆还是维护小顶堆
                heapq.heappush(hp, nums[i])  # push进一个元素 堆还是维护小顶堆
        return hp[0]
