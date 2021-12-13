# 517. 超级洗衣机
from typing import List


class Solution:
    # def findMinMoves(self, machines: List[int]) -> int:
    #     tot = sum(machines)
    #     n = len(machines)
    #     if tot % n:
    #         return -1
    #     avg = tot // n
    #     ans, s = 0, 0
    #     for num in machines:
    #         num -= avg
    #         s += num  # s 的最终结果也是 0
    #         ans = max(ans, abs(s), num)
    #     return ans

    # https://leetcode-cn.com/problems/super-washing-machines/solution/acmjin-pai-ti-jie-tan-xin-bian-cheng-xio-mp7n/
    # def findMinMoves(self, machines: List[int]) -> int:
    #     tol = sum(machines)
    #     n = len(machines)
    #     if tol % n:
    #         return -1
    #     avg = tol // n
    #     pre_sum = 0
    #     res = 0
    #     # 其中 m-avg 不需要绝对值，因为本来就最少需要移动 max(machines)-avg 次数
    #     for i, m in enumerate(machines):
    #         pre_sum += m
    #         res = max(res, abs(pre_sum-(i+1)*avg), m-avg)
    #     return res

    def findMinMoves(self, machines: List[int]) -> int:
        n = len(machines)
        tol = sum(machines)
        if tol % n:
            return -1
        avg = tol // n
        pre_sum = 0
        res = 0
        for i, m in enumerate(machines):
            pre_sum += m
            res = max(res, abs(pre_sum-(i+1)*avg), m-avg)
        return res


s = Solution()
machines = [1,0,5]
print(s.findMinMoves(machines))

machines = [0,3,0]
print(s.findMinMoves(machines))

machines = [0,2,0]
print(s.findMinMoves(machines))

machines = [0, 0, 11, 5]
print(s.findMinMoves(machines))
