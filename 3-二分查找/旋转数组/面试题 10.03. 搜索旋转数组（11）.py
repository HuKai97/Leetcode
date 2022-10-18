class Solution:
    def search(self, arr: List[int], target: int) -> int:
        # 找到某个元素  arr元素可能重复  重复就返回idx最小的那个
        if not arr: return -1
        left, right = 0, len(arr) - 1
        while left <= right:
            # left符合时  直接返回  因为找到的就是最小的
            if arr[left] == target: return left
            mid = left + (right - left) // 2
            # mid符合时  right->mid  因为左边可能还有target的值
            if arr[mid] == target:
                right = mid
            elif arr[mid] > arr[right]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < arr[right]:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                # 相等时 重复 right -= 1
                right -= 1
        return -1