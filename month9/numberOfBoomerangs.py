# 447. 回旋镖的数量
from typing import List
from collections import defaultdict


class Solution:
    # 暴力法
    # 排序数 A，下标是 m，上标是 2，结果是 v * (v-1)
    # 其中 p 是中心点
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for p in points:
            dic = defaultdict(int)
            for q in points:
                k = (p[0]-q[0]) ** 2 + (p[1]-q[1]) ** 2
                dic[k] += 1
            for v in dic.values():
                res += v * (v-1)
        return res


s = Solution()
points = [[0,0],[1,0],[2,0]]
print(s.numberOfBoomerangs(points))

points = [[1,1],[2,2],[3,3]]
print(s.numberOfBoomerangs(points))

points = [[1,1]]
print(s.numberOfBoomerangs(points))
