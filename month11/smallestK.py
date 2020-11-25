# 最小 K 个数
from typing import List
import heapq

class Solution:
    def smallestK(self, arr: List[int], k: int) -> List[int]:
        if not arr or not k:
            return []
        queue = [-x for x in arr[:k]]
        heapq.heapify(queue)
        for num in arr[k:]:
            if -num > queue[0]:
                heapq.heappushpop(queue, -num)
        return [-x for x in queue]


s = Solution()
arr = [1,3,5,7,2,4,6,8]
k = 4
print(s.smallestK(arr, k))
