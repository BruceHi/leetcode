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

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     return [x for x, _ in count.most_common(k)]

    # 时间复杂度为 O(n log k)，超过 95%
    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     arr = [(val, key) for key, val in count.items()]  # 次数，实际值
    #     queue = arr[:k]
    #     heapq.heapify(queue)
    #     for x, y in arr[k:]:
    #         if x > queue[0][0]:
    #             heapq.heappushpop(queue, (x, y))
    #     return [x[1] for x in queue]

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     return [x for x, _ in count.most_common(k)]

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     count = Counter(nums)
    #     arr = [(v, key) for key, v in count.items()]
    #     queue = arr[:k]
    #     heapq.heapify(queue)
    #     for key, val in arr[k:]:
    #         if key > queue[0][0]:
    #             heapq.heappushpop(queue, (key, val))
    #     return [x for _, x in queue]

    # def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    #     counter = Counter(nums)
    #     return [x[0] for x in counter.most_common(k)]

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        arr = [(v, key) for key, v in count.items()]

        queue = arr[:k]
        heapq.heapify(queue)
        for v, key in arr[k:]:
            if v > queue[0][0]:
                heapq.heappushpop(queue, (v, key))
        return [x[1] for x in queue]


s = Solution()
nums = [1,1,1,2,2,3]
k = 2
print(s.topKFrequent(nums, k))

nums = [1]
k = 1
print(s.topKFrequent(nums, k))


nums = [3,0,1,0]
k = 1
print(s.topKFrequent(nums, k))
