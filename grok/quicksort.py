# 快速排序（因为快，所以叫这个名字），要求原地排序

# 递归，非原地排序(不太合适)
# def quicksort(nums):
#     if len(nums) < 2:  # 包括 1 和 0 的情况
#         return nums
#     pivot = nums[0]  # 选取第一个为基线条件，也可以选择最后一个
#     less = [i for i in nums[1:] if i <= pivot]
#     greater = [i for i in nums[1:] if i > pivot]
#     return quicksort(less) + [pivot] + quicksort(greater)


# # 原地排序  选取
# def partition(arr, left, right):
#     pivot, j = arr[left], left
#     for i in range(left+1, right+1):
#         if arr[i] <= pivot:  # i 永远是跑得快的，遇见小的，就与 j （右面）前面一位的数交换。注意 = 号。
#             j += 1  # j 指向的永远是小于或等于 pivot 的值，而他前面的不是。
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[left], arr[j] = arr[j], arr[left]
#     return j  # 分类好数据，并返回分类的位置点

# def partition(arr, left, right):
#     pivot, j = arr[left], left+1
#     for i in range(left+1, right+1):
#         if arr[i] <= pivot:
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1
#     arr[left], arr[j-1] = arr[j-1], arr[left]
#     return j-1  # 分类好数据，并返回分类的位置点

# 原地排序  推荐使用右边的数为基准值

# def partition(arr, left, right):  # 选取最右边的数为基准值
#     pivot, j = arr[right], left
#     for i in range(left, right):
#         if arr[i] < pivot:  # j 停在了小的地方
#             arr[i], arr[j] = arr[j], arr[i]  # 然后交换
#             j += 1  # j 指向的永远是大于 pivot 的值，即待交换位置。j 停在了大的地方。
#     arr[right], arr[j] = arr[j], arr[right]
#     return j
#
#
# def quicksort(arr, left=None, right=None):
#     # 第一次进行调用的时候，left 和 right 没有进行赋值，要进行特殊处理。
#     if left is None:
#         left = 0
#     if right is None:  # 不能写成 not right, 如果 right = 0 时，right 就会被重新赋值为 arr 整个长度（很长） - 1.
#         right = len(arr) - 1
#     if left < right:  # 排序条件
#         p = partition(arr, left, right)
#         quicksort(arr, left, p-1)
#         quicksort(arr, p+1, right)
#     return arr

# def quicksort(arr, left=None, right=None):
#     if left is None:
#         left = 0
#     if right is None:
#         right = len(arr) - 1
#     if left < right:
#         p = partition(arr, left, right)
#         quicksort(arr, left, p-1)
#         quicksort(arr, p+1, right)
#     return arr
#
#
# def partition(arr, left, right):
#     pivot, j = arr[right], left
#     for i in range(left, right):
#         if arr[i] < pivot:
#             arr[i], arr[j] = arr[j], arr[i]
#             j += 1
#     arr[j], arr[right] = arr[right], arr[j]
#     return j

from typing import List


# def quick_sort(nums: List[int], left=None, right=None) -> List[int]:
#     if left is None:
#         left = 0
#     if right is None:
#         right = len(nums) - 1
#     if left < right:
#         p = partition(nums, left, right)
#         quick_sort(nums, left, p-1)
#         quick_sort(nums, p+1, right)
#     return nums
#
#
# def partition(nums: List[int], left: int, right: int) -> int:
#     pivot, j = nums[right], left
#     for i in range(left, right):
#         if nums[i] < pivot:
#             nums[i], nums[j] = nums[j], nums[i]
#             j += 1
#     nums[j], nums[right] = pivot, nums[j]
#     return j

# left, right 都是 int 类型，代表区间
# def quick_sort(nums, left=None, right=None):
#     if left is None and right is None:
#         left, right = 0, len(nums) - 1
#     if left < right:
#         p = partition(nums, left, right)
#         quick_sort(nums, left, p-1)
#         quick_sort(nums, p+1, right)
#     return nums
#
#
# def partition(nums, left, right):
#     pivot, i = nums[right], left
#     for j in range(left, right):
#         if nums[j] < pivot:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#     nums[i], nums[right] = pivot, nums[i]
#     return i

# left, right 表示要排序的区间范围
# def quick_sort(nums: List[int], left=None, right=None) -> List[int]:
#     if left is None and right is None:
#         left, right = 0, len(nums) - 1
#     if left < right:
#         p = partition(nums, left, right)
#         quick_sort(nums, left, p-1)
#         quick_sort(nums, p+1, right)
#     return nums
#
#
# def partition(nums: List[int], left: int, right: int) -> int:
#     pivot, i = nums[right], left
#     for j in range(left, right):
#         if nums[j] < pivot:  # 小于交换
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#     nums[i], nums[right] = pivot, nums[i]
#     return i

# def quick_sort(nums: List[int], left: int = None, right: int = None):
#     if left is None and right is None:
#         left, right = 0, len(nums) - 1
#     if left < right:
#         p = partition(nums, left, right)
#         quick_sort(nums, left, p - 1)
#         quick_sort(nums, p + 1, right)
#     return nums
#
#
# def partition(nums: List[int], left: int, right: int):
#     i, pivot = left, nums[right]
#     for j in range(left, right):
#         if nums[j] < pivot:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#     nums[i], nums[right] = pivot, nums[i]
#     return i

# def quick_sort(nums, left=None, right=None):
#     if left is None and right is None:
#         left, right = 0, len(nums) - 1
#     if left < right:
#         p = partition(nums, left, right)
#         quick_sort(nums, left, p-1)
#         quick_sort(nums, p+1, right)
#     return nums
#
#
# def partition(nums, left, right):
#     i, pivot = left, nums[right]
#     for j in range(left, right):  # left 也要算在内
#         if nums[j] < pivot:
#             nums[i], nums[j] = nums[j], nums[i]
#             i += 1
#     nums[i], nums[right] = pivot, nums[i]
#     return i

def quick_sort(nums, left=None, right=None):
    if left is None and right is None:
        left, right = 0, len(nums)-1
    if left < right:
        p = partition(nums, left, right)
        quick_sort(nums, left, p-1)
        quick_sort(nums, p+1, right)
    return nums


def partition(nums, left, right):
    pivot, i = nums[right], left
    for j in range(left, right):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[right] = pivot, nums[i]
    return i


num = [5, 8, 9, 1, 2]
print(quick_sort(num))
print(num)

nums = []
print(quick_sort(nums))

nums = [1]
print(quick_sort(nums))

nums = [1, 4, 5, 6, 5, 6]
print(quick_sort(nums))
