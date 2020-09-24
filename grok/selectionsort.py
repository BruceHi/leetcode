# 选择排序 不稳定、原地算法。O(n^2)
# def find_smallest(arr):
#     small = float('inf')
#     small_index = None
#     for i, v in enumerate(arr):
#         if v < small:
#             small = v
#             small_index = i
#     return small_index


# def select_sort(arr):  # array的缩写
#     for i in range(len(arr)):
#         # j = find_smallest(arr[i:])  # 这样写的话，返回值可能小于当前的i
#         j = i + find_smallest(arr[i:])
#         arr[i], arr[j] = arr[j], arr[i]

# 简洁写法
# def select_sort(arr):  # 当 nums 为空的时候，什么都不执行。没有返回值，相当于返回值是None.
#     for i in range(len(arr)):
#         min_index = i
#         min_val = arr[i]
#         for j in range(i, len(arr)):
#             if arr[j] < min_val:
#                 min_val = arr[j]
#                 min_index = j
#         arr[i], arr[min_index] = arr[min_index], arr[i]

# 改进
# 选择排序，不稳定，比如[1, 6, 7, 6, 3, 4] 中第一个出现的 6 就被交换到第二次出现的 6 后面了。

from typing import List


# def select_sort(nums: List[int]) -> List[int]:
#     n = len(nums)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1, n):
#             if nums[min_index] > nums[j]:
#                 min_index = j
#         nums[i], nums[min_index] = nums[min_index], nums[i]
#     return nums

# def select_sort(nums: List[int]) -> List[int]:
#     for i, num in enumerate(nums[:-1]):
#         min_num = num
#         idx = i
#         for j in range(i, len(nums)):
#             if min_num > nums[j]:
#                 min_num = nums[j]
#                 idx = j
#         nums[i], nums[idx] = min_num, num
#     return nums

def select_sort(nums: List[int]) -> List[int]:
    for i, num in enumerate(nums[:-1]):
        idx = i
        for j in range(i+1, len(nums)):
            if nums[idx] > nums[j]:
                idx = j
        nums[i], nums[idx] = nums[idx], num
    return nums


nums = [7, 5, 9, 6, 2]
select_sort(nums)
print(nums)

nums = []
select_sort(nums)
print(nums)

nums = [1, 4, 5, 6, 5, 6]
select_sort(nums)
print(nums)


