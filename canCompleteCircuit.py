# 134.加油站
from typing import List


class Solution:
    # 暴力法通过了，竟然没有超时
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     n = len(gas)
    #     for i in range(n):
    #         if gas[i] >= cost[i]:
    #             remain = gas[i] - cost[i]
    #             j = i
    #             while True:
    #                 j = (j + 1) % n
    #                 remain += gas[j] - cost[j]
    #                 if remain < 0:
    #                     break
    #                 if i == j % n:
    #                     return i
    #     return -1

    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     if sum(gas) - sum(cost) < 0:
    #         return -1
    #     cur, res = 0, 0
    #     for i in range(len(gas)):
    #         cur += gas[i] - cost[i]
    #         if cur < 0:
    #             cur = 0
    #             res = i + 1
    #     return res

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total, cur, res = 0, 0, 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                res = i + 1
        return res if total >= 0 else -1


s = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
print(s.canCompleteCircuit(gas, cost))

gas = [2,3,4]
cost = [3,4,3]
print(s.canCompleteCircuit(gas, cost))
