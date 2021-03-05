# 836. 矩阵重叠
# 使用反向思维，先求不重叠的情况
from typing import List


class Solution:
    # def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    #     if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:  # 去掉一条线的情况
    #         return False
    #     return not(rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1])

    # 更清晰
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec1[0] == rec1[2] or rec1[1] == rec1[3] or rec2[0] == rec2[2] or rec2[1] == rec2[3]:  # 去掉一条线的情况
            return False
        x_overlap = not(rec1[2] <= rec2[0] or rec2[2] <= rec1[0])
        y_overlap = not(rec1[3] <= rec2[1] or rec2[3] <= rec1[1])
        return x_overlap and y_overlap


s = Solution()
rec1 = [0,0,2,2]
rec2 = [1,1,3,3]
print(s.isRectangleOverlap(rec1, rec2))

rec1 = [0,0,1,1]
rec2 = [1,0,2,1]
print(s.isRectangleOverlap(rec1, rec2))

rec1 = [0,0,1,1]
rec2 = [2,2,3,3]
print(s.isRectangleOverlap(rec1, rec2))

rec1 = [-1,0,1,1]
rec2 = [0,-1,0,1]
print(s.isRectangleOverlap(rec1, rec2))
