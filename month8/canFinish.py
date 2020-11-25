# 课程表
from typing import List
from functools import lru_cache
from collections import defaultdict
from collections import deque

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

    # # 深度优先搜索，不太直观
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     visited = [0] * numCourses
    #     # edges = defaultdict(int)  # 有的课程编号就为 0，有的没有前驱节点的出现的也会是 0，不能用 int
    #     edges = defaultdict(list)
    #     for cur, pre in prerequisites:
    #         edges[pre].append(cur)
    #
    #     @lru_cache(None)
    #     def dfs(i):  # i 代表课程编号
    #         if visited[i]:
    #             return False
    #         visited[i] = 1
    #         for j in edges[i]:
    #             if not dfs(j):
    #                 return False
    #         visited[i] = 0
    #         return True
    #
    #     for i in range(numCourses):
    #         if not dfs(i):
    #             return False
    #     return True

    # # 拓扑排序，使用广度优先搜索，更为直观
    # def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    #     edges = defaultdict(list)
    #     in_degree = [0] * numCourses  # 入度
    #
    #     for cur, pre in prerequisites:
    #         edges[pre].append(cur)
    #         in_degree[cur] += 1
    #
    #     queue = deque([cur for cur in range(numCourses) if not in_degree[cur]])
    #     visited = 0  # 访问的节点个数，以便后续判断
    #
    #     while queue:
    #         visited += 1
    #         u = queue.popleft()
    #         for v in edges[u]:
    #             in_degree[v] -= 1  # 修改当前节点的入度
    #             if not in_degree[v]:
    #                 queue.append(v)
    #     return visited == numCourses

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = defaultdict(list)
        in_degree = [0] * numCourses

        for cur, pre in prerequisites:
            edges[pre].append(cur)
            in_degree[cur] += 1

        # range(numCourses) 不能改成 edges，因为可能有些点是孤立的，并不在 prerequisites 记录中，但是入度为 0
        queue = deque([cur for cur in range(numCourses) if not in_degree[cur]])
        visited = 0

        while queue:
            visited += 1
            u = queue.popleft()
            for v in edges[u]:
                in_degree[v] -= 1
                if not in_degree[v]:
                    queue.append(v)
        return visited == numCourses


s = Solution()
print(s.canFinish(2, [[1,0]]))

print(s.canFinish(2, [[1,0],[0,1]]))

print(s.canFinish(3, [[1,0],[2,1]]))

print(s.canFinish(3, [[0, 1], [1, 2], [2, 0]]))

print(s.canFinish(3, [[2, 1], [2, 0], [1, 0]]))

print(s.canFinish(4, [[2, 1], [2, 0], [1, 0], [3, 0], [3, 2]]))

print(s.canFinish(1, []))
