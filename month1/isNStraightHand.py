# 846. 一手顺子
from typing import List
from collections import Counter


class Solution:
    # 通过
    # def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
    #     n = len(hand)
    #     if n % groupSize:
    #         return False
    #
    #     group_num = n // groupSize
    #     groups = [[] for _ in range(group_num)]
    #
    #     hand.sort()
    #     for h in hand:
    #         for g in groups:
    #             if not g or len(g) < groupSize and h == g[-1] + 1:
    #                 g.append(h)
    #                 break
    #     return all([len(g) == groupSize for g in groups])

    # 注意一定要排序，从小牌开始拿起
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        hand.sort()
        count = Counter(hand)
        for h in hand:
            if count[h] == 0:
                continue
            for x in range(h, h+groupSize):
                if count[x] == 0:
                    return False
                count[x] -= 1
        return True


s = Solution()
hand = [1,2,3,6,2,3,4,7,8]
groupSize = 3
print(s.isNStraightHand(hand, groupSize))

hand = [1,2,3,4,5]
groupSize = 4
print(s.isNStraightHand(hand, groupSize))

hand = [2, 1]
groupSize = 2
print(s.isNStraightHand(hand, groupSize))
