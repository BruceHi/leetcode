# 165. 比较版本号
from itertools import zip_longest


class Solution:
    # def compareVersion(self, version1: str, version2: str) -> int:
    #     nums1, nums2 = version1.split('.'), version2.split('.')
    #     n1, n2 = len(nums1), len(nums2)
    #     n = max(n1, n2)
    #     for i in range(n):
    #         num1 = int(nums1[i]) if i < n1 else 0
    #         num2 = int(nums2[i]) if i < n2 else 0
    #         if num1 < num2:
    #             return -1
    #         if num1 > num2:
    #             return 1
    #     return 0

    # def compareVersion(self, version1: str, version2: str) -> int:
    #     nums1, nums2 = version1.split('.'), version2.split('.')
    #     m, n = len(nums1), len(nums2)
    #     for i in range(max(m, n)):
    #         num1 = int(nums1[i]) if i < m else 0
    #         num2 = int(nums2[i]) if i < n else 0
    #         if num1 < num2:
    #             return -1
    #         if num1 > num2:
    #             return 1
    #     return 0

    def compareVersion(self, version1: str, version2: str) -> int:
        # fillvalue 默认是 None
        for v1, v2 in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            num1, num2 = int(v1), int(v2)
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0


s = Solution()
version1 = "1.01"
version2 = "1.001"
print(s.compareVersion(version1, version2))

version1 = "1.0"
version2 = "1.0.0"
print(s.compareVersion(version1, version2))

version1 = "0.1"
version2 = "1.1"
print(s.compareVersion(version1, version2))

version1 = "1.0.1"
version2 = "1"
print(s.compareVersion(version1, version2))

version1 = "7.5.2.4"
version2 = "7.5.3"
print(s.compareVersion(version1, version2))
