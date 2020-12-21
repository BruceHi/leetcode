# 剑指 offer 40. 最小的 k 个数
from typing import List
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k:
            return []
        queue = [-num for num in arr[:k]]
        heapq.heapify(queue)
        for num in arr[k:]:
            if -num > queue[0]:
                heapq.heappushpop(queue, -num)
        return [-num for num in queue]


s = Solution()
arr = [3,2,1]
k = 2
print(s.getLeastNumbers(arr, k))

arr = [0,1,2,1]
k = 1
print(s.getLeastNumbers(arr, k))

arr = [0,0,0,2,0,5]
k = 0
print(s.getLeastNumbers(arr, k))
