# 数组中的第K个最大元素
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k-1]


s = Solution()
nums = [3,2,1,5,6,4]
k = 2
print(s.findKthLargest(nums, k))

nums = [3,2,3,1,2,4,5,5,6]
k = 4
print(s.findKthLargest(nums, k))