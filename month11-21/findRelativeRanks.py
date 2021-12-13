# 506. 相对名次
from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        dic = {}
        for i, sc in enumerate(sorted(score, reverse=True)):
            if i == 0:
                dic[sc] = "Gold Medal"
            elif i == 1:
                dic[sc] = "Silver Medal"
            elif i == 2:
                dic[sc] = "Bronze Medal"
            else:
                dic[sc] = str(i+1)
        return [dic[sc] for sc in score]



s = Solution()
score = [5,4,3,2,1]
print(s.findRelativeRanks(score))

score = [10,3,8,9,4]
print(s.findRelativeRanks(score))
