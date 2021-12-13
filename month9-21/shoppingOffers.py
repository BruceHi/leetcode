# 638. 大礼包
from typing import List


class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        pass

s = Solution()
price = [2,5]
special = [[3,0,5],[1,2,10]]
needs = [3,2]
print(s.shoppingOffers(price, special, needs))

price = [2,3,4]
special = [[1,1,0,4],[2,2,1,9]]
needs = [1,2,1]
print(s.shoppingOffers(price, special, needs))
