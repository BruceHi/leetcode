# 667. 优美的排列 2
from typing import List


class Solution:
    # def constructArray(self, n: int, k: int) -> List[int]:
    #     res = list(range(1, n-k))
    #     i, j = n - k, n
    #     while i <= j:
    #         res.append(i)
    #         if i != j:
    #             res.append(j)
    #         i, j = i + 1, j - 1
    #     return res

    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, n-k))
        i, j = n - k, n
        while i <= j:
            res.append(i)
            if i != j:
                res.append(j)
            i, j = i + 1, j - 1
        return res


s = Solution()
n = 3
k = 1
print(s.constructArray(n, k))

n = 3
k = 2
print(s.constructArray(n, k))

n = 6
k = 5
print(s.constructArray(n, k))