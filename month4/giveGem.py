# 宝石补给
from typing import List


class Solution:
    # def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
    #     for a, b in operations:
    #         v = gem[a] // 2
    #         gem[a] -= v
    #         gem[b] += v
    #     return max(gem) - min(gem)

    def giveGem(self, gem: List[int], operations: List[List[int]]) -> int:
        for i, j in operations:
            v = gem[i] // 2
            gem[i] -= v
            gem[j] += v
        return max(gem) - min(gem)


s = Solution()
gem = [3,1,2]
operations = [[0,2],[2,1],[2,0]]
print(s.giveGem(gem, operations))

gem = [100,0,50,100]
operations = [[0,2],[0,1],[3,0],[3,0]]
print(s.giveGem(gem, operations))

gem = [0,0,0,0]
operations = [[1,2],[3,1],[1,2]]
print(s.giveGem(gem, operations))
