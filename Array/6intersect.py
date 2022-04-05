# 两个数组的交集
from typing import List
from collections import Counter

# hash表，统计出一个词频的用法
# def intersect(nums1, nums2):
#
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
#
#     m = {}
#     for i in range(len(nums1)):
#         m[nums1[i]] = m.get(nums1[i], 0) + 1
#
#     k = 0
#     for i in nums2:
#         if i in m and m[i] > 0:
#             nums1[k] = i    # 重复利用了nums1，不用另建空间
#             k += 1
#             m[i] -= 1
#
#     return nums1[:k]

# def intersect(nums1, nums2):
#     if len(nums1) > len(nums2):
#         nums1, nums2 = nums2, nums1
#     dic = Counter(nums1)  # 统计词频
#     res = []
#     for i in nums2:
#         if dic.get(i):
#             dic[i] -= 1
#             res.append(i)
#
#     return res


# 排序
# def intersect(nums1, nums2):
#     nums1.sort()
#     nums2.sort()
#     res = []
#     i, j = 0, 0
#     while i < len(nums1) and j < len(nums2):
#         if nums1[i] == nums2[j]:
#             res.append(nums1[i])
#             i, j = i+1, j+1
#         elif nums1[i] > nums2[j]:
#             j += 1
#         else:
#             i += 1
#     return res

# 统计两个词频的用法
# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     dic1, dic2 = Counter(nums1), Counter(nums2)
#     res = []
#     for num in dic1:
#         if num in dic2:
#             res += [num] * min(dic1[num], dic2[num])
#     return res

# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     dic1, dic2 = Counter(nums1), Counter(nums2)
#     res = []
#     for k1, v1 in dic1.items():
#         if k1 in dic2:
#             res += [k1] * min(v1, dic2[k1])
#     return res

# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     return list((Counter(nums1) & Counter(nums2)).elements())


# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     inter = set(nums1) & set(nums2)
#     res = []
#     for i in inter:
#         res += [i] * min(nums1.count(i), nums2.count(i))
#     return res

# def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
#     count1, count2 = Counter(nums1), Counter(nums2)
#     return list((count1 & count2).elements())

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count1, count2 = Counter(nums1), Counter(nums2)
        return list((count1 & count2).elements())


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersect(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersect(nums1, nums2))
