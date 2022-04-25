# 386. 字典树排序
from typing import List


class Solution:
    # nlogn
    # def lexicalOrder(self, n: int) -> List[int]:
    #     return sorted(range(1, n+1), key=str)

    # 时间复杂度是 O(n)
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(i):
            if i > n:
                return
            res.append(i)
            for j in range(10):
                dfs(i*10 + j)

        for i in range(1, 10):
            dfs(i)
        return res



s = Solution()
n = 13
print(s.lexicalOrder(n))

n = 2
print(s.lexicalOrder(n))

