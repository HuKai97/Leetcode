"""
@Author: HuKai
@Date: 2022/5/26  11:25
@github: https://github.com/HuKai97
"""
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 异常判断
        if len(nums) == 0: return -1
        if nums[0] > target or nums[-1] < target: return -1
        # 开始搜， 事先假定target在闭区间[begin, end]
        left, right = 0, len(nums) - 1
        # 开始二分查找，这里使用排除法， 先排除不可能的区间，那么看循环结束条件变了
        # 注意此时不能有等于了，因为我们这里是排除不可能区间
        # 那么当begin==end的时候，此时只剩下一个元素，要么是我们要的，要么不是，但此时要退出，不用再找，已经得到结果
        while left < right:
            mid = left + (right - left) // 2   # 取左中位数
            # 这里不能判断等于的情况，因为我们用的排除思维，只需要排除目标一定不在的元素区间
            # 此时说明目标元素一定不在mid及其左边，排除掉
            if nums[mid] < target: left = mid + 1
            # 这是nums[mid] >= target的情况，说明目标在mid及左边, 往左缩小
            else: right = mid
        # 退出循环，要么找到，要么没找到，如果找到的话，left和right都指向它了
        return left if nums[left] == target else -1


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 异常判断
        if len(nums) == 0: return -1
        if nums[0] > target or nums[-1] < target : return -1
        # 开始搜， 事先假定target在闭区间[begin, end]
        left, right = 0, len(nums) - 1
        # 开始二分查找，这里使用排除法， 先排除不可能的区间，那么看循环结束条件变了
        # 注意此时不能有等于了，因为我们这里是排除不可能区间
        # 那么当begin==end的时候，此时只剩下一个元素，要么是我们要的，要么不是，但此时要退出，不用再找，已经得到结果
        while left < right:
            mid = left + (right - left + 1) // 2    # 取右中位数
            # 这里不能判断等于的情况，因为我们用的排除思维，只需要排除目标一定不在的元素区间
            # 此时# 说明一定在左边了，此时排除掉mid及其右边
            if nums[mid] > target: right = mid - 1
            # 这是nums[mid] <= target的情况，# 说明在mid及其右边，所以排除掉左边
            else: left = mid
        # 退出循环，要么找到，要么没找到，如果找到的话，left和right都指向它了
        return left if nums[left] == target else -1

# 不常用 只在leetcode33.搜索旋转排序数组中用到
def BinarySearch(nums, target):
    # 异常判断
    if len(nums) == 0:  return -1
    if target < nums[0] or target > nums[-1]: return -1

    # 开始搜， 注意我们假定target在一个闭区间[begin, end], 那么一开始的搜索范围
    begin, end = 0, len(nums) - 1  # 这个end最后一个元素所在位置，这时候搜索值肯定在这个闭区间中

    # 开始二分查找
    while begin <= end:  # [begin, end] 这里要注意是小于等于，当begin==end，区间[begin, end]依然有效

        mid = begin + (end - begin) // 2  # 这里要防止溢出现象，还有种更优雅的写法 mid = begin + ((end - begin) >> 1)

        if num[mid] == target:  # 这里找到目标值了, 返回位置
            return mid
        elif nums[mid] > target:  # 说明target在mid左边，这时候搜索范围变为[begin, mid-1], 始终保持闭区间搜索
            end = mid - 1
        else:  # 说明target在mid右边， 这时候搜索范围[mid+1, end], 始终保持闭区间搜索
            begin = mid + 1

    # 退出循环的时候，说明没有找到元素，返回-1
    return -1
