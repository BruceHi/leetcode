# 1627. 最富有客户的资产总量
from typing import List


class Solution:
    # def maximumWealth(self, accounts: List[List[int]]) -> int:
    #     res = 0
    #     for a in accounts:
    #         res = max(res, sum(a))
    #     return res

    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))


s = Solution()
accounts = [[1,2,3],[3,2,1]]
print(s.maximumWealth(accounts))

accounts = [[1,5],[7,3],[3,5]]
print(s.maximumWealth(accounts))

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(s.maximumWealth(accounts))
