# 最接近原点的 K 个点
# small k
from typing import List
from collections import defaultdict
from math import sqrt
import heapq


class Solution:
    # 构建排序规则
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     res = sorted(points, key=lambda x: x[0]**2 + x[1]**2)
    #     return res[:K]

    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     dic = defaultdict(list)
    #     for x, y in points:
    #         dist = x**2 + y**2
    #         dic[dist].append([x, y])
    #
    #     queue = []
    #     for key, values in dic.items():
    #         for v in values:
    #             queue.append((key, v))
    #     heapq.heapify(queue)
    #     res = [x[1] for x in heapq.nsmallest(K, queue)]
    #     return res

    # 使用堆，改进，时间复杂度还是 O(n log n)
    # def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    #     queue = []
    #     for x, y in points:
    #         dist = x**2 + y**2
    #         queue.append((dist, [x, y]))
    #
    #     heapq.heapify(queue)
    #     res = [x[1] for x in heapq.nsmallest(K, queue)]
    #     return res

    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        nums = []
        for x, y in points:
            dist = x**2 + y**2
            nums.append((-dist, [x, y]))

        queue = nums[:K]
        heapq.heapify(queue)
        for d, x in nums[K:]:
            if d > queue[0][0]:
                heapq.heappushpop(queue, (d, x))
        res = [x[1] for x in queue]
        return res


s = Solution()
points = [[1,3],[-2,2]]
K = 1
print(s.kClosest(points, K))

points = [[3,3],[5,-1],[-2,4]]
K = 2
print(s.kClosest(points, K))
