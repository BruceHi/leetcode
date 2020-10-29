# 找到 K 个最接近的元素
from typing import List


class Solution:

    # 删除 n-k 个元素
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

    # 二分法，不明白为什么要 mid + k 进行比较，以后要多看几遍
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     left, right = 0, len(arr) - k
    #     while left < right:
    #         mid = left + right >> 1
    #         if x - arr[mid] > arr[mid + k] - x:
    #             left = mid + 1
    #         else:
    #             right = mid
    #     return arr[left:left + k]

    # # 按差值绝对值排序，时间复杂度是 O(n log n)
    # def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    #     nums = [(abs(num - x), num) for num in arr]
    #     res = sorted(nums)[:k]
    #     return sorted([num[1] for num in res])

    # https://leetcode-cn.com/problems/find-k-closest-elements/solution/pai-chu-fa-shuang-zhi-zhen-er-fen-fa-python-dai-ma/
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        while left < right:
            mid = left + right >> 1
            if x - arr[mid] > arr[mid + k] - x:  # 不能添加 abs，否则最后一个示例错了
                left = mid + 1
            else:
                right = mid
        return arr[right: right+k]


s = Solution()
nums = [1,2,3,4,5]
k=4
x=3
print(s.findClosestElements(nums, k, x))

nums = [1,2,3,4,5]
k=4
x=-1
print(s.findClosestElements(nums, k, x))

nums = [1,1,1,10,10,10]
k = 1
x = 9
print(s.findClosestElements(nums, k, x))

nums = [1,1,2,2,2,2,2,3,3]
k = 3
x = 3
print(s.findClosestElements(nums, k, x))
