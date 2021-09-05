# 插入排序：原地排序，稳定
from typing import List


# def insert_sort(nums: List[int]) -> List[int]:
#     for i in range(1, len(nums)):
#         val = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > val:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = val
#     return nums

# def insert_sort(nums: List[int]) -> List[int]:
#     for i in range(1, len(nums)):
#         tmp = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > tmp:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = tmp
#     return nums

# def insert_sort(nums):
#     for i in range(1, len(nums)):
#         num = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > num:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = num

# def insert_sort(nums):
#     n = len(nums)
#     for i in range(1, n):
#         j = i
#         while j-1 >= 0 and nums[j] < nums[j-1]:
#             nums[j], nums[j-1] = nums[j-1], nums[j]
#             j -= 1
#     return nums

# def insert_sort(nums):
#     for i in range(1, len(nums)):
#         num = nums[i]
#         j = i - 1
#         while j >= 0 and nums[j] > num:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = num
#     return nums

# def insert_sort(nums):
#     for i in range(1, len(nums)):
#         num = nums[i]
#         j = i
#         while j-1 >= 0 and nums[j-1] > num:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = num
#     return nums

# def insert_sort(nums):
#     n = len(nums)
#     for i, num in enumerate(nums):
#         j = i
#         while j-1 >= 0 and num < nums[j-1]:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = num

# def insert_sort(nums):
#     n = len(nums)
#     for i in range(1, n):
#         num = nums[i]
#         j = i - 1
#         while j >= 0 and num < nums[j]:
#             nums[j+1] = nums[j]
#             j -= 1
#         nums[j+1] = num
#     return nums

# def insert_sort(nums):
#     n = len(nums)
#     for i in range(1, n):
#         j = i
#         val = nums[i]
#         while j-1 >= 0 and nums[j-1] > val:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = val

# def insert_sort(nums):
#     n = len(nums)
#     for i in range(1, n):
#         j = i
#         tmp = nums[i]
#         while j-1 >= 0 and nums[j-1] > tmp:
#             nums[j] = nums[j-1]
#             j -= 1
#         nums[j] = tmp

def insert_sort(nums):
    pass

nums = [7, 5, 9, 6, 2]
insert_sort(nums)
print(nums)

nums = []
insert_sort(nums)
print(nums)

nums = [1]
insert_sort(nums)
print(nums)

nums = [1, 4, 5, 6, 5, 6]
insert_sort(nums)
print(nums)
