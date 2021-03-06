# 两个数组的交集
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2,2]
print(s.intersection(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(s.intersection(nums1, nums2))
