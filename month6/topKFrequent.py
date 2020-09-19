# 前 K 个高频元素
from typing import List
from collections import Counter
import heapq


class Solution:
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     return sorted(count, key=count.get, reverse=True)[:k]

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     return heapq.nlargest(k, count, key=count.get)

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        return [x for x, _ in count.most_common(k)]


s = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s.topKFrequent(nums, k))

nums = [1]
k = 1
print(s.topKFrequent(nums, k))
