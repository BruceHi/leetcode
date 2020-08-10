# 课程表
from typing import List
from functools import lru_cache
from collections import defaultdict


class Solution:

    # # # 应该正确，但超出时间限制
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     # @lru_cache(None) 不能使用 cache，因为 cur 不能哈希
    #     def dfs(i, num, cur):
    #         if num in cur:
    #             return False
    #         cur.append(num)
    #         idx = [x for x, arr in enumerate(prerequisites) if arr[0] == prerequisites[i][1] and x != i]
    #         if not idx:
    #             return True
    #         return dfs(idx[0], prerequisites[i][1], cur)
    #
    #     for i, arr in enumerate(prerequisites):
    #         if not dfs(i, arr[0], []):
    #             return False
    #
    #     return True

    # # 错误答案，忽视了 1 个课表可能有 不止一个 前驱课表
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     visited = [0] * (numCourses + 1)
    #
    #     def dfs(i):
    #         if visited[prerequisites[i][0]]:
    #             return False
    #         idx = [x for x, arr in enumerate(prerequisites) if arr[0] == prerequisites[i][1] and x != i]
    #         if not idx:
    #             return True
    #         visited[prerequisites[i][0]] = 1
    #         return dfs(idx[0])
    #
    #     for i, nums in enumerate(prerequisites):
    #         if not visited[nums[0]]:
    #             if not dfs(i):
    #                 return False
    #     return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        # edges = defaultdict(int)  # 有的课程编号就为 0，有的没在出现的也会是 0，不能用 int
        edges = defaultdict(list)
        for cur, pre in prerequisites:
            edges[pre].append(cur)

        @lru_cache(None)
        def dfs(i):  # i 代表课程编号
            if visited[i]:
                return False
            visited[i] = 1
            for j in edges[i]:
                if not dfs(j):
                    return False
            visited[i] = 0
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True




s = Solution()
print(s.canFinish(2, [[1,0]]))

print(s.canFinish(2, [[1,0],[0,1]]))

print(s.canFinish(3, [[1,0],[2,1]]))

print(s.canFinish(3, [[0, 1], [1, 2], [2, 0]]))

print(s.canFinish(3, [[2, 1], [2, 0], [1, 0]]))

print(s.canFinish(4, [[2, 1], [2, 0], [1, 0], [3, 0], [3, 2]]))
