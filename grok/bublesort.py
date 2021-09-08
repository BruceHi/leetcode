# 冒泡排序
# def bubulesort(nums):
#     n = len(nums)
#     for j in range(n-1):  # 总共比较 n-1 次
#         for i in range(n-1-j):  # 每次比较的元素个数，每次 i 要到的最后索引不超过 n-1-j
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]


# 冒泡排序, 改进

from typing import List


# def bubule_sort(nums: List[int]) -> List[int]:
#     n = len(nums)
#     for j in range(n-1):
#         swap = False
#         for i in range(n-1-j):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 swap = True
#         if not swap:
#             break
#     return nums

# def bubule_sort(nums: List[int]) -> List[int]:
#     n = len(nums)
#     for j in range(n-1):
#         swap = False
#         for i in range(n-1-j):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 swap = True
#         if not swap:
#             break
#     return nums

# def bubule_sort(nums):
#     n = len(nums)
#     for i in range(n-1):
#         swap = False
#         for j in range(n-i-1):
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#                 swap = True
#         if not swap:
#             break

# def bubule_sort(nums):
#     n = len(nums)
#     for i in range(n-1):  # 轮次
#         change = False
#         for j in range(n-1-i):  # 元素比较
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#                 change = True
#         if not change:
#             break
#     return nums

# def bubule_sort(nums):
#     n = len(nums)
#     for j in range(n-1):
#         swap = False
#         for i in range(n-1-j):
#             if nums[i] > nums[i+1]:
#                 nums[i], nums[i+1] = nums[i+1], nums[i]
#                 swap = True
#         if not swap:
#             break
#     return nums

# def bubule_sort(nums):
#     n = len(nums)
#     for i in range(n-1):
#         swap = False
#         for j in range(n-1-i):
#             if nums[j] > nums[j+1]:
#                 swap = True
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#         if not swap:
#             break

# def bubule_sort(nums):
#     n = len(nums)
#     for i in range(n-1):
#         swap = False
#         for j in range(n-1-i):
#             if nums[j] > nums[j+1]:
#                 swap = True
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#         if not swap:
#             break

def bubule_sort(nums):
    n = len(nums)
    for i in range(n-1):
        swap = False
        for j in range(n-1-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                swap = True
            if not swap:
                return


nums = [7, 5, 9, 6, 2]
bubule_sort(nums)
print(nums)

nums = []
bubule_sort(nums)
print(nums)

nums = [1]
bubule_sort(nums)
print(nums)

nums = [1, 4, 5, 6, 5, 6]
bubule_sort(nums)
print(nums)
