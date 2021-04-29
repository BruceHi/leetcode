# 归并排序，空间复杂度 O(n)，非原地排序
from typing import List


# def merge_sort(nums: List[int]) -> List[int]:
#     n = len(nums)
#     if n < 2:
#         return nums
#     mid = n >> 1
#     left, right = nums[:mid], nums[mid:]
#     return merge(merge_sort(left), merge_sort(right))
#
#
# def merge(left: List[int], right: List[int]) -> List[int]:
#     res = []
#     n1, n2 = len(left), len(right)
#     i, j = 0, 0
#     while i < n1 and j < n2:
#         if left[i] <= right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     if i < n1:
#         res += left[i:]
#     if j < n2:
#         res += right[j:]
#     return res

# def merge_sort(nums: List[int]) -> List[int]:
#     n = len(nums)
#     if n < 2:
#         return nums
#     mid = n >> 1
#     left, right = nums[:mid], nums[mid:]
#     return merge(merge_sort(left), merge_sort(right))
#
#
# def merge(left: List[int], right: List[int]) -> List[int]:
#     m, n = len(left), len(right)
#     i, j = 0, 0
#     res = []
#     while i < m and j < n:
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     if i < m:
#         res.extend(left[i:])
#     if j < n:
#         res.extend(right[j:])
#     return res


# def merge_sort(nums: List[int]) -> List[int]:
#     n = len(nums)
#     if n < 2:
#         return nums
#     mid = n >> 1
#     return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))
#
# #
# def merge(left: List[int], right: List[int]):
#     m, n = len(left), len(right)
#     i, j = 0, 0
#     res = []
#     while i < m and j < n:
#         if left[i] < right[j]:
#             res.append(left[i])
#             i += 1
#         else:
#             res.append(right[j])
#             j += 1
#     if i < m:
#         res.extend(left[i:])
#     if j < n:
#         res.extend(right[j:])
#     return res

# def merge_sort(nums):
#     n = len(nums)
#     if n < 2:
#         return nums
#     mid = n >> 1
#     return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))
#
#
# def merge(nums1, nums2):
#     m, n = len(nums1), len(nums2)
#     i, j = 0, 0
#     res = []
#     while i < m and j < n:
#         if nums1[i] < nums2[j]:
#             res.append(nums1[i])
#             i += 1
#         else:
#             res.append(nums2[j])
#             j += 1
#     if i < m:
#         res.extend(nums1[i:])
#     if j < n:
#         res.extend(nums2[j:])
#     return res

def merge_sort(nums):
    n = len(nums)
    if n <= 1:
        return nums
    mid = n >> 1
    return merge(merge_sort(nums[:mid]), merge_sort(nums[mid:]))


def merge(nums1, nums2):
    m, n = len(nums1), len(nums2)
    i, j = 0, 0
    res = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    if i < m:
        res.extend(nums1[i:])
    if j < n:
        res.extend(nums2[j:])
    return res





num = [5, 8, 9, 1, 2]
print(merge_sort(num))

nums = []
print(merge_sort(nums))

nums = [1]
print(merge_sort(nums))

nums = [1, 4, 5, 6, 5, 6]
print(merge_sort(nums))
