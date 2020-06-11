from typing import List


class Solution:
    # def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
    #     res = []
    #     max_val = max(candies)
    #     for c in candies:
    #         if max_val - c > extraCandies:
    #             res.append(False)
    #         else:
    #             res.append(True)
    #     return res

    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_val = max(candies)
        return [max_val - c <= extraCandies for c in candies]


s = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(s.kidsWithCandies(candies, extraCandies))

candies = [4,2,1,1,2]
extraCandies = 1
print(s.kidsWithCandies(candies, extraCandies))

candies = [12,1,12]
extraCandies = 10
print(s.kidsWithCandies(candies, extraCandies))