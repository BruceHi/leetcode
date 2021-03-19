# 452. 用最少数量的箭引爆地球
from typing import List


class Solution:
    # 失败
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     if not points:
    #         return 0
    #     res = 1
    #     points.sort()
    #     i, j = 0, 1
    #     while j < len(points):
    #         if points[i][0] <= points[j][0] <= points[i][1]:
    #             res += 0
    #         else:
    #             res += 1
    #             i = j
    #         j += 1
    #     return res

    # 失败
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     if not points:
    #         return 0
    #     res = 1
    #     points.sort()
    #     i, j = 0, 1
    #     while j < len(points):
    #         if points[j][0] > points[i][1]:
    #             res += 1
    #             i = j
    #         j += 1
    #     return res

    # 按左侧排序
    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     if not points:
    #         return 0
    #     res = 1
    #     points.sort()
    #     min_right = points[0][1]
    #     for j in range(1, len(points)):
    #         if points[j][0] > min_right:
    #             res += 1
    #             min_right = points[j][1]
    #         else:
    #             min_right = min(min_right, points[j][1])
    #     return res

    # 按右侧排序
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x:x[1])
        res = 1
        pos = points[0][1]  # 右顶点
        for point in points[1:]:
            if point[0] > pos:
                res += 1
                pos = point[1]
        return res

    # def findMinArrowShots(self, points: List[List[int]]) -> int:
    #     if not points:
    #         return 0
    #     points.sort(key=lambda x:x[1])
    #     res = 1
    #     pos = points[0][1]  # 右顶点
    #     for left, right in points:
    #         if left > pos:
    #             res += 1
    #             pos = right
    #     return res


s = Solution()
points = [[10,16],[2,8],[1,6],[7,12]]
print(s.findMinArrowShots(points))

points = [[1,2],[3,4],[5,6],[7,8]]
print(s.findMinArrowShots(points))

points = [[1,2],[2,3],[3,4],[4,5]]
print(s.findMinArrowShots(points))

points = [[1,2]]
print(s.findMinArrowShots(points))

points = [[2,3],[2,3]]
print(s.findMinArrowShots(points))

points = [[9,12],[1,10],[4,11],[8,12],[3,9],[6,9],[6,7]]
print(s.findMinArrowShots(points))
