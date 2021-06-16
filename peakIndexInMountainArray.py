# 852. 山脉数组的峰顶索引
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        while left < right:
            mid = left + right >> 1
            if arr[mid] < arr[mid+1]:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution()
arr = [0,1,0]
print(s.peakIndexInMountainArray(arr))

arr = [0,2,1,0]
print(s.peakIndexInMountainArray(arr))

arr = [0,10,5,2]
print(s.peakIndexInMountainArray(arr))

arr = [3,4,5,1]
print(s.peakIndexInMountainArray(arr))

arr = [24,69,100,99,79,78,67,36,26,19]
print(s.peakIndexInMountainArray(arr))
