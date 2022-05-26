"""
@Author: HuKai
@Date: 2022/5/26  10:04
@github: https://github.com/HuKai97
"""
# 1、归并排序
# https://www.bilibili.com/video/BV1Ax411U7Xx?spm_id_from=333.337.search-card.all.click
# 分治：一开始先把数组从中间划分成两个子数组，一直递归地把子数组划分成更小的子数组，直到子数组里面只有一个元素，才开始排序。
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

# nums = [4, 2, 3, 6, 1, 7]
# nums = merge_sort(nums)
# print(nums)  # [1, 2, 3, 4, 6, 7]

# 2、快速排序
# 思想：小于idx的数放在idx左边  大于idx的数放在idx右边
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quick_sort(nums, left, right):
            if left >= right: return  # 如果只有一个元素了，返回
            temp = left   # 中轴  下面交换过程中中轴的数不变
            i, j = left, right
            while i < j:
                # 注意这里要先比较j  再比较i
                while i < j and nums[j] > nums[temp]: j -= 1  # 从右边找比中轴小的数
                while i < j and nums[i] <= nums[temp]: i += 1   # 从左边找比中轴大的数
                nums[i], nums[j] = nums[j], nums[i]
            # # 把中轴放到有序的位置上， 使得左边的元素小于中轴，右边的元素大于中轴 i=j
            nums[temp], nums[i] = nums[i], nums[temp]
            quick_sort(nums, left, i-1)
            quick_sort(nums, i+1, right)
        quick_sort(nums, 0, len(nums)-1)
        return nums



# 3、堆排序
# https://www.bilibili.com/video/BV1Eb41147dK?spm_id_from=333.337.search-card.all.click
# 最大堆  自己实现
def heapify(tree, n, i):  # tree[i]为根节点的子树进行堆排序
    c1 = 2 * i + 1
    c2 = 2 * i + 2
    max_index = i  # 小顶堆这里改下
    if c1 < n and tree[c1] > tree[max_index]:  # 小顶堆这里改下
        max_index = c1
    if c2 < n and tree[c2] > tree[max_index]:
        max_index = c2
    if max_index != i:
        tree[max_index], tree[i] = tree[i], tree[max_index]
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
        tree[i], tree[0] = tree[0], tree[i]
        heapify(tree, i, 0)
# nums = [3, 2, 1, 5, 6, 4]
# heap_sort(nums, len(nums))
# print(nums)  # [1, 2, 3, 4, 5, 6]

# import heapq
# nums = [3, 2, 1, 5, 6, 4]
# heapq.heapify(nums)   # 第一种掉包排序实现（建立最小堆）
# print(nums)  # [1, 2, 3, 5, 6, 4]
# hp = []
# for num in nums:      # 第二种掉包堆排序实现（建立最小堆）
#     heapq.heappush(hp, num)   # push进一个元素 堆还是维护小顶堆
#
# min_val = heapq.heappop(nums)  # 弹出堆顶元素（最小值） 堆还是维护小顶堆


