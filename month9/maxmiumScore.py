from typing import List
from functools import lru_cache


class Solution:
    # 超时
    # def maxmiumScore(self, cards: List[int], cnt: int) -> int:
    #     res = 0
    #     n = len(cards)
    #
    #     def dfs(start, cur):
    #         nonlocal res
    #         if len(cur) == cnt:
    #             sum_card = sum(cur)
    #             if not sum_card & 1:
    #                 res = max(res, sum_card)
    #             return
    #
    #         for i in range(start, n + 1-(cnt-len(cur))):
    #             dfs(i+1, cur+[cards[i]])
    #
    #     dfs(0, [])
    #     return res

    # 超时
    # def maxmiumScore(self, cards: List[int], cnt: int) -> int:
    #     res = 0
    #     n = len(cards)
    #
    #     @lru_cache(None)
    #     def dfs(start, next, end):
    #         nonlocal res
    #         if next == cnt:
    #             if not end & 1:
    #                 res = max(res, end)
    #             return
    #
    #         for i in range(start, n + 1-(cnt-next)):
    #             dfs(i+1, next+1, end+cards[i])
    #
    #     dfs(0, 0, 0)
    #     return res

    def maxmiumScore(self, cards: List[int], cnt: int) -> int:
        res = 0
        n = len(cards)

        @lru_cache(None)
        def dfs(start, next, end):
            nonlocal res
            if next == cnt:
                if not end & 1:
                    res = max(res, end)
                return

            for i in range(start, n + 1-(cnt-next)):
                dfs(i+1, next+1, end+cards[i])

        dfs(0, 0, 0)
        return res


s = Solution()
cards = [1,2,8,9]
cnt = 3
print(s.maxmiumScore(cards, cnt))

cards = [3,3,1]
cnt = 1
print(s.maxmiumScore(cards, cnt))
