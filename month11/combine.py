# 77. 组合
from typing import List
from itertools import combinations


class Solution:
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     return list(map(list, combinations(range(1, n+1), k)))

    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     return list(map(list, combinations(range(1, n+1), k)))

    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     res = []
    #
    #     def dfs(start, cur):
    #         if len(cur) == k:
    #             res.append(cur)
    #             return
    #         # for i in range(start, n+1):
    #         for i in range(start, n + 2-(k-len(cur))):  # 优化 需要3个，则最后剩余2个不取就行，若取了的话，下次递归就取不到了
    #             dfs(i+1, cur+[i])
    #
    #     dfs(1, [])
    #     return res

    # 因为 path 是全局变量，res.append() 所有的值都是 path，path 改变，所有值都会变化
    # 只有递，归由 pop 提供。
    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     res = []
    #     path = []
    #
    #     def backtrack(num_index):
    #         if len(path) == k:
    #             res.append(path[:])
    #             # print(res)
    #             return
    #         for i in range(num_index, n + 1):
    #             path.append(i)
    #             backtrack(i + 1)
    #             path.pop()
    #
    #     backtrack(1)
    #     return res

    # def combine(self, n: int, k: int) -> List[List[int]]:
    #     res = []
    #
    #     def dfs(i, cur):
    #         if len(cur) == k:
    #             res.append(cur)
    #             return
    #         for j in range(i+1, n+1):
    #             if j not in cur:
    #                 dfs(j, cur + [j])
    #     dfs(0, [])
    #     return res

    def combine(self, n: int, k: int) -> List[List[int]]:
        return list(map(list, combinations(range(1, n+1), k)))


s = Solution()
n = 4
k = 2
print(s.combine(n, k))

n = 1
k = 1
print(s.combine(n, k))

n = 5
k = 4
print(s.combine(n, k))