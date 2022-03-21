# 杨辉三角
from typing import List
from functools import reduce


class Solution:
    # def generate(self, numRows: int) -> List[List[int]]:
    #     if not numRows:
    #         return []
    #
    #     res = [[1]]
    #     i = 1
    #     while i < numRows:
    #         pop = res[-1]
    #         tmp = []
    #         for j in range(1, len(pop)):
    #             tmp.append(pop[j] + pop[j-1])
    #         res.append([1] + tmp + [1])
    #         i += 1
    #     return res

    # 生成法
    # def generate(self, numRows: int) -> List[List[int]]:
    #     if not numRows:
    #         return []
    #
    #     res = [[1]]
    #     for _ in range(numRows-1):
    #         pop = res[-1]
    #         tmp = []
    #         for i in range(1, len(pop)):
    #             tmp.append(pop[i-1] + pop[i])
    #         res.append([1] + tmp + [1])
    #     return res

    # 动态规划
    # def generate(self, numRows: int) -> List[List[int]]:
    #     triangle = []
    #     for i in range(numRows):
    #         row = [1] * (i + 1)
    #         for j in range(1, i):  # 只计算除首尾地方的数。i 相当于 len(row) - 1
    #             row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    #         triangle.append(row)
    #     return triangle

    # 错位相加
    # def generate(self, numRows: int) -> List[List[int]]:
    #     if not numRows:
    #         return []
    #
    #     res = [[1]]
    #     for _ in range(numRows-1):
    #         tmp = [x+y for x, y in zip([0] + res[-1], res[-1] + [0])]
    #         res.append(tmp)
    #     return res

    # def generate(self, numRows: int) -> List[List[int]]:
    #     if not numRows:
    #         return []
    #     res = [[1]]
    #     for _ in range(numRows-1):  # 循环次数
    #         tmp = [x + y for x, y in zip([0] + res[-1], res[-1] + [0])]
    #         res.append(tmp)
    #     return res

    # def generate(self, numRows: int) -> List[List[int]]:
    #     triangle = []
    #     for i in range(numRows):
    #         row = [1] * (i+1)
    #         for j in range(1, i):
    #             row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    #         triangle.append(row)
    #     return triangle

    # def generate(self, numRows: int) -> List[List[int]]:
    #     if numRows == 1:
    #         return [[1]]
    #     res = [[1]]
    #     for _ in range(numRows-1):
    #         tmp = [x + y for x, y in zip([0] + res[-1], res[-1] + [0])]
    #         res.append(tmp)
    #     return res

    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1]]
        for i in range(1, numRows):
            row = [1] * (i+1)
            for j in range(1, i):
                row[j] = triangle[i-1][j] + triangle[i-1][j-1]
            triangle.append(row)
        return triangle


s = Solution()
print(s.generate(5))

print(s.generate(1))
