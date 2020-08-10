# 寻找两个正序数组的中位数，二分查找的方法暂时不会
from typing import List


class Solution:

    # 结果是要将两个排序数组合并后取中位数，并非分别求中位数再平均。时间复杂度是 O(m+n)
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #
    #     nums = []
    #
    #     def merge(nums1, nums2):
    #         if not nums1:
    #             nums.extend(nums2)
    #             return
    #         if not nums2:
    #             nums.extend(nums1)
    #             return
    #         if nums1[0] < nums2[0]:
    #             nums.append(nums1[0])
    #             nums1[:] = nums1[1:]
    #             merge(nums1, nums2)  # 没有返回值，只能这样调用
    #         else:
    #             nums.append(nums2[0])
    #             nums2[:] = nums2[1:]
    #             merge(nums1, nums2)
    #
    #     merge(nums1, nums2)
    #
    #     n = len(nums)
    #     if n & 1:
    #         return nums[n // 2]
    #     else:
    #         return (nums[n // 2] + nums[n // 2 - 1]) / 2

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def merge(nums1, nums2):
            if not nums1:
                return nums2
            if not nums2:
                return nums1
            if nums1[0] < nums2[0]:
                return [nums1[0]] + merge(nums1[1:], nums2)
            return [nums2[0]] + merge(nums1, nums2[1:])

        nums = merge(nums1, nums2)
        n = len(nums)
        if n & 1:
            return nums[n // 2]
        else:
            return (nums[n // 2] + nums[n // 2 - 1]) / 2


s = Solution()
nums1 = [1, 3]
nums2 = [2]
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = [1, 2]
nums2 = [3, 4]
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = [1]
nums2 = [3]
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = []
nums2 = [3]
print(s.findMedianSortedArrays(nums1, nums2))

nums1 = [4, 5, 7]
nums2 = []
print(s.findMedianSortedArrays(nums1, nums2))