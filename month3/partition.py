# 131. 分隔回文串
from typing import List
from itertools import combinations


class Solution:
    # def partition(self, s: str) -> List[List[str]]:
    #     n = len(s)
    #
    #     def dfs(i, cur):
    #         if i == n:
    #             res.append(cur)
    #             return
    #         for j in range(i+1, n+1):
    #             tmp = s[i:j]
    #             if tmp == tmp[::-1]:
    #                 dfs(j, cur+[tmp])
    #
    #     res = []
    #     dfs(0, [])
    #     return res

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        def dfs(i, cur):
            if i == n:
                res.append(cur)
                return
            for j in range(i+1, n+1):
                tmp = s[i:j]
                if tmp == tmp[::-1]:
                    dfs(j, cur+[tmp])

        res = []
        dfs(0, [])
        return res


obj = Solution()
s = "aab"
print(obj.partition(s))

s = "a"
print(obj.partition(s))
