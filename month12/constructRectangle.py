# 构造矩形
from  typing import List
from math import sqrt


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        for x in range(int(sqrt(area)), 0, -1):
            if area % x == 0:
                return [area//x, x]


s = Solution()
area = 4
print(s.constructRectangle(area))

area = 5
print(s.constructRectangle(area))

area = 6
print(s.constructRectangle(area))
