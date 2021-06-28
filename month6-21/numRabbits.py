# 781. 森林中的兔子
from typing import List
from collections import Counter


class Solution:
    # 如果有 x 只兔子都回答 y，则至少有 取上整(x/(y+1)) 种不同颜色，每种颜色有 y+1 只兔子，
    # 因此兔子数最少为：取上整(x/(y+1)) * y+1
    # (x + (y - 1)) / y 是x/y向上取整，把y换y+1就x/(y+1)向上取整
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        return sum((x+y)//(y+1)*(y+1) for y, x in count.items())  # x 为 数量，y为其他颜色


s = Solution()
answers = [1, 1, 2]
print(s.numRabbits(answers))

answers = [10, 10, 10]
print(s.numRabbits(answers))

answers = []
print(s.numRabbits(answers))

