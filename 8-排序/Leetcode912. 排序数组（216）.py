"""
@Author: HuKai
@Date: 2022/5/26  10:35
@github: https://github.com/HuKai97
"""
# 0、堆排序
# 0、完全二叉树  2、父节点大于子节点
# https://www.bilibili.com/video/BV1Eb41147dK?spm_id_from=333.337.search-card.all.click
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def heapify(tree, n, i):  # tree[i]为根节点的子树进行堆排序
            c1 = 2 * i + 1
            c2 = 2 * i + 2
            max_index = i  # 小顶堆这里改下
            if c1 < n and tree[c1] > tree[max_index]:  # 小顶堆这里改下
                max_index = c1
            if c2 < n and tree[c2] > tree[max_index]:
                max_index = c2
            if max_index != i:
                # tree[max_index], tree[i] = tree[i], tree[max_index]
                tree[i], tree[max_index] = tree[max_index], tree[i]
                # max_index和i作了交换，所以max_index分支需要重新整理为大顶堆
                heapify(tree, n, max_index)
        def build_heap(tree, n):   # 从parent->0节点分别进行一次堆排序 就建立了这个树的堆
            last_node = n - 1
            parent = (last_node - 1) // 2
            for i in range(parent, -1, -1):
                heapify(tree, n, i)
        def heap_sort(tree, n):
            build_heap(tree, n)
            for i in range(n-1, -1, -1):
                tree[i], tree[0] = tree[0], tree[i]  # 把最大值放到最后
                heapify(tree, i, 0)   # 从根节点开始heapify 但是个数为n-0
        heap_sort(nums, len(nums))
        return nums



# 2、归并排序
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            # 合并两个有序数组
            m, n = len(left), len(right)
            merge_arr = [0 for _ in range(m + n)]
            # 从后往前遍历，进行合并
            while m and n:
                if left[m - 1] > right[n - 1]:
                    merge_arr[m + n - 1] = left[m - 1]
                    m -= 1
                else:
                    merge_arr[m + n - 1] = right[n - 1]
                    n -= 1
            if m:
                merge_arr[:m] = left[:m]
            if n:
                merge_arr[:n] = right[:n]
            return merge_arr

        def merge_sort(nums):
            if len(nums) <= 1: return nums
            mid = len(nums) // 2
            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])
            return merge(left, right)

        return merge_sort(nums)


# 2、快排  超时了  为什么？？？
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums, left, right):
            if left >= right: return
            temp = left
            i, j = left, right
            while i < j:
                while i < j and nums[j] > nums[temp]: j -= 1
                while i < j and nums[i] <= nums[temp]: i += 1
                nums[i], nums[j] = nums[j], nums[i]
            nums[temp], nums[i] = nums[i], nums[temp]
            quick_sort(nums, left, i-1)
            quick_sort(nums, i+1, right)
        quick_sort(nums, 0, len(nums)-1)
        return nums