# 剑指 offer 17. 打印从 1 到最大的 n 位数
from typing import List


class Solution:
    # 没有列表生成式快
    # def printNumbers(self, n: int) -> List[int]:
    #     return [i for i in range(1, 10**n)]

    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10**n))

s = Solution()
n = 1
print(s.printNumbers(n))

n = 2
print(s.printNumbers(n))

n = 3
print(s.printNumbers(n))

n = 4
print(s.printNumbers(n))
