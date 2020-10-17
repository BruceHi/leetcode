# 统计从0 到 n 的所有数含 1 的个数。
from typing import List


class Solution:
    # def countBits(self, num: int):
    #     res = []
    #     for n in range(num+1):
    #         count = 0
    #         while n:
    #             count += 1
    #             n = n & (n-1)
    #         res.append(count)
    #     return res

    # def countBits(self, num: int):
    #     res = [0] * (num+1)
    #     for i in range(1, num+1):
    #         res[i] = res[i & i-1] + 1  # 抹去末尾 1 之后，前面肯定有存储的，直接使用就行，不必再遍历。
    #     return res

    # def countBits(self, num: int) -> List[int]:
    #     res = []
    #     for i in range(num+1):
    #         count = 0
    #         while i:
    #             count += 1
    #             i &= i - 1
    #         res.append(count)
    #     return res

    def countBits(self, num: int) -> List[int]:
        res = [0] * (num+1)
        for i in range(1, num+1):
            res[i] = res[i & i-1] + 1
        return res


s = Solution()
n = 2
print(s.countBits(n))

n = 5
print(s.countBits(n))
