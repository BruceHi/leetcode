# 1046. 最后一块石头的重量
# 使用大顶堆
from typing import List


class Solution:
    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     n = len(stones)
    #     while n > 1:
    #         stones.sort(reverse=True)
    #         val = stones[0] - stones[1]
    #         if val:
    #             stones = stones[2:] + [val]
    #             n -= 1
    #         else:
    #             stones = stones[2:]
    #             n -= 2
    #     return stones[0] if stones else 0

    # def lastStoneWeight(self, stones: List[int]) -> int:
    #     while len(stones) > 1:
    #         stones.sort(reverse=True)
    #         val = stones[0] - stones[1]
    #         if val:
    #             stones = stones[2:] + [val]
    #         else:
    #             stones = stones[2:]
    #     return stones[0] if stones else 0

    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort(reverse=True)
            val = stones[0] - stones[1]
            if val:
                stones = stones[2:] + [val]
            else:
                stones = stones[2:]
        return stones[0] if stones else 0


s = Solution()
stones = [2,7,4,1,8,1]
print(s.lastStoneWeight(stones))

stones = [2, 2]
print(s.lastStoneWeight(stones))