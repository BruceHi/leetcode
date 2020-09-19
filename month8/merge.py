# 合并两个有序数组到 nums1
from typing import List


class Solution:
    # 递归
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
    #     def merge_two(nums1, nums2):
    #         if not nums1:
    #             return nums2
    #         if not nums2:
    #             return nums1
    #         if nums1[0] < nums2[0]:
    #             return [nums1[0]] + merge_two(nums1[1:], nums2)
    #         return [nums2[0]] + merge_two(nums1, nums2[1:])
    #
    #     nums = merge_two(nums1[:m], nums2)
    #     nums1[:m+n] = nums

    # 迭代
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     tmp = nums1[:m]
    #     nums1[:] = []  # 必须是切片赋值
    #     i = j = 0
    #
    #     while i < m and j < n:
    #         if tmp[i] < nums2[j]:
    #             nums1.append(tmp[i])
    #             i += 1
    #         else:
    #             nums1.append(nums2[j])
    #             j += 1
    #
    #     if i < m:
    #         nums1.extend(tmp[i:])
    #     if j < n:
    #         nums1.extend(nums2[j:])

    # # 迭代，从前往后遍历，空间复杂度为 O(m)，由于要复制一份 nums1[:m]
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     nums1_copy = nums1[:m]
    #     nums1[:] = []  # 必须是切片赋值
    #     i, j = 0, 0
    #
    #     while i < m and j < n:
    #         if nums1_copy[i] < nums2[j]:
    #             nums1.append(nums1_copy[i])
    #             i += 1
    #         else:
    #             nums1.append(nums2[j])
    #             j += 1
    #
    #     if i < m:
    #         nums1 += nums1_copy[i:]
    #     if j < n:
    #         nums1 += nums2[j:]

    # 迭代，从后往前遍历，不占用额外空间，空间复杂度是 O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        i, j = m-1, n-1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1

        if j >= 0:
            nums1[:p+1] = nums2[:j+1]


s = Solution()
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
s.merge(nums1, m, nums2, n)
print(nums1)

nums1 = [0]
m = 0
nums2 = [1]
n = 1
s.merge(nums1, m, nums2, n)
print(nums1)
