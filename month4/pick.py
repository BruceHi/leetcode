# 398. 随机数索引
from typing import List
from collections import defaultdict
from random import choice


class Solution:

    def __init__(self, nums: List[int]):
        self.dic = defaultdict(list)
        for i, num in enumerate(nums):
            self.dic[num].append(i)

    def pick(self, target: int) -> int:
        return choice(self.dic[target])


nums = [1,2,3,3,3]
s = Solution(nums)
print(s.pick(3))
print(s.pick(1))
