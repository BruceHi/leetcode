# 210.课程表 二
from typing import List
from collections import defaultdict, deque


class Solution:
    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     in_degree = [0] * numCourses
    #     graph = defaultdict(list)
    #
    #     for suc, pre in prerequisites:
    #         graph[pre].append(suc)
    #         in_degree[suc] += 1
    #     queue = deque(i for i in range(numCourses) if not in_degree[i])  # 不能写成 in in_degree
    #
    #     res = []
    #     while queue:
    #         pre = queue.popleft()
    #         res.append(pre)
    #         for suc in graph[pre]:
    #             in_degree[suc] -= 1
    #             if not in_degree[suc]:
    #                 queue.append(suc)
    #     return res if len(res) == numCourses else []  # 最后一句是判定是否有环，有环肯定不能遍历完。

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        edges = defaultdict(list)
        in_degree = [0] * numCourses

        for cur, pre in prerequisites:
            edges[pre].append(cur)
            in_degree[cur] += 1

        queue = deque([pre for pre in range(numCourses) if in_degree[pre] == 0])
        res = []

        while queue:
            u = queue.popleft()
            res.append(u)
            for v in edges[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.append(v)
        return res if len(res) == numCourses else []


s = Solution()
numCourses = 2
prerequisites = [[1,0]]
print(s.findOrder(numCourses, prerequisites))

numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(s.findOrder(numCourses, prerequisites))

numCourses = 2
prerequisites = []
print(s.findOrder(numCourses, prerequisites))

numCourses = 3
prerequisites = [[1,0]]
print(s.findOrder(numCourses, prerequisites))

numCourses = 3
prerequisites = [[1,0],[1,2],[0,1]]
print(s.findOrder(numCourses, prerequisites))  # 有环，返回 []
