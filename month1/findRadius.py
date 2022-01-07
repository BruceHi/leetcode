# 475. 供暖器
from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        pass


s = Solution()
houses = [1,2,3]
heaters = [2]
print(s.findRadius(houses, heaters))

houses = [1,2,3,4]
heaters = [1,4]
print(s.findRadius(houses, heaters))

houses = [1,5]
heaters = [2]
print(s.findRadius(houses, heaters))
