# 剑指 offer 66. 构建乘积数组
from typing import List


class Solution:
    # 超时
    # def constructArr(self, a: List[int]) -> List[int]:
    #     if not a:
    #         return []
    #
    #     pre = [1]
    #     for num in a[:-1]:
    #         pre.append(num * pre[-1])
    #    # 估计大量拼接比较费时
    #     suc = [1]
    #     for num in reversed(a[1:]):
    #         suc = [num * suc[0]] + suc
    #
    #     res = []
    #     for x, y in zip(pre, suc):
    #         res.append(x * y)
    #     return res

    # 扫描两遍不超时
    # def constructArr(self, a: List[int]) -> List[int]:
    #     if not a:
    #         return []
    #     res = [1]
    #     for num in a[:-1]:
    #         res.append(num*res[-1])
    #
    #     tmp = 1
    #     for i in range(len(a)-1, -1, -1):
    #         res[i] = res[i] * tmp
    #         tmp *= a[i]
    #
    #     return res

    # 不超时
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        left, right = [1] * n, [1] * n
        res = [1] * n

        for i in range(1, n):
            left[i] = left[i-1] * a[i-1]

        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * a[i+1]

        for i in range(n):
            res[i] = left[i] * right[i]
        return res


s = Solution()
a = [1,2,3,4,5]
print(s.constructArr(a))

a = []
print(s.constructArr(a))

a = [1]
print(s.constructArr(a))

a = [2]
print(s.constructArr(a))

print([1] * 0)
