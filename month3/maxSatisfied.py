# 1052.爱生气的书店老板
from typing import List


class Solution:
    # def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
    #     n = len(customers)
    #     total = 0
    #     for c, g in zip(customers, grumpy):
    #         if g == 0:
    #             total += c
    #
    #     cur = 0  # 不让人满意的数量
    #     for i in range(X):
    #         if grumpy[i] == 1:
    #             cur += customers[i]
    #     res = cur  # 记录不让人满意数量的最大值
    #     for i in range(X, n):
    #         if grumpy[i] == 1:  # 进入生气
    #             cur += customers[i]
    #         if grumpy[i-X] == 1:  # 离开的那个格子生气
    #             cur -= customers[i-X]
    #         res = max(res, cur)
    #     return total + res

    # 人数与是否生气相乘，可以简化运算
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        n = len(customers)
        total = 0
        for c, g in zip(customers, grumpy):
            if g == 0:
                total += c

        cur = 0  # 不让人满意的数量
        for i in range(X):
            cur += customers[i] * grumpy[i]
        res = cur  # 记录不让人满意数量的最大值

        for i in range(X, n):
            cur += customers[i] * grumpy[i] - customers[i-X] * grumpy[i-X]
            res = max(res, cur)
        return total + res


s = Solution()
customers = [1,0,1,2,1,1,7,5]
grumpy = [0,1,0,1,0,1,0,1]
X = 3
print(s.maxSatisfied(customers, grumpy, X))
