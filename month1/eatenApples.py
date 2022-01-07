# 1705. 吃苹果的最大数目
from typing import List
# from heapq import heappop, heappush
import heapq

class Solution:
    # 错误方法
    # def eatenApples(self, apples: List[int], days: List[int]) -> int:
    #     remain = 0
    #     res = 0
    #     for i, (a, d) in enumerate(zip(apples, days)):
    #         n = min(a, d)
    #         if n < remain:
    #             remain -= 1
    #         else:
    #             res += n - remain
    #             remain = n - 1
    #
    #         if remain < 0:
    #             remain = 0
    #
    #     return res

    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        heap = []
        n = len(apples)
        mx = max([i + days[i] for i in range(n)])
        ans = 0
        for i in range(mx):
            if i < n and apples[i]:
                heapq.heappush(heap, (i + days[i], apples[i]))
            while heap:
                day, apple = heapq.heappop(heap)
                if day > i and apple > 0:
                    if apple - 1 > 0:
                        heapq.heappush(heap, (day, apple - 1))
                    ans += 1
                    break
        return ans

    # def eatenApples(self, apples: List[int], days: List[int]) -> int:
    #     heap = []
    #     n = len(apples)
    #     res = 0
    #     i = 0
    #     while i < n or heap:
    #         if heap and heap[0][0] <= i:
    #             heapq.heappop(heap)
    #         if i < n and apples[i]:
    #             heapq.heappush(heap, [i+days[i], apples[i]])
    #         if heap:
    #             heap[0][1] -= 1
    #             res += 1
    #             if heap[0][1] == 0:
    #                 heapq.heappop(heap)
    #         i += 1
    #     return res



s = Solution()
apples = [1,2,3,5,2]
days = [3,2,1,4,2]
print(s.eatenApples(apples, days))

apples = [3,0,0,0,0,2]
days = [3,0,0,0,0,2]
print(s.eatenApples(apples, days))
