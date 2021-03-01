# 分糖果2
from typing import List


class Solution:
    # def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    #     res = [0] * num_people
    #     i = 0
    #     while candies > 0:
    #         res[i % num_people] += min(i+1, candies)
    #         candies -= i + 1  # 最后一次 candies 是 0 或负数
    #         i += 1
    #     return res

    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0] * num_people
        i = 0
        while candies > 0:
            res[i % num_people] += min(i+1, candies)
            candies -= i + 1
            i += 1
        return res


s = Solution()
candies = 7
num_people = 4
print(s.distributeCandies(candies, num_people))

candies = 10
num_people = 3
print(s.distributeCandies(candies, num_people))
