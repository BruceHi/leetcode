# 找到 K 个最接近的元素
from typing import List


class Solution:

    # 使用 hash 表，并排序，时间复杂度是 O(n log n)
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     dic = {}
    #     for i, num in enumerate(arr):
    #         dic[i] = abs(num - x)
    #     a = sorted(dic, key=dic.get)[:k]
    #     return arr[min(a): max(a)]


    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     n = len(arr)
    #     left, right = 0, n - 1
    #
    #     remove = n - k
    #     while remove:
    #         if x - arr[left] <= arr[right] - x:
    #             right -= 1
    #         else:
    #             left += 1
    #         remove -= 1
    #     return arr[left:right + 1]

    # 二分法，不明白为什么要 mid + k 进行比较
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + right >> 1
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left:left + k]


s = Solution()
nums = [1,2,3,4,5]
k=4
x=3
print(s.findClosestElements(nums, k, x))

nums = [1,2,3,4,5]
k=4
x=-1
print(s.findClosestElements(nums, k, x))