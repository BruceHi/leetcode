# 398. 随机数索引
from typing import List
from collections import defaultdict
from random import choice


# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.dic = defaultdict(list)
#         for i, num in enumerate(nums):
#             self.dic[num].append(i)
#
#     def pick(self, target: int) -> int:
#         return choice(self.dic[target])

# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.dic = defaultdict(list)
#         for i, num in enumerate(nums):
#             self.dic[num].append(i)
#
#     def pick(self, target: int) -> int:
#         return choice(self.dic[target])

# class Solution:
#
#     def __init__(self, nums: List[int]):
#         self.dic = defaultdict(list)
#         for i, num in enumerate(nums):
#             self.dic[num].append(i)
#
#     def pick(self, target: int) -> int:
#         return choice(self.dic[target])

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


def print_func(funs, attrs):
    res = [None]
    obj = eval(funs[0])(*attrs[0])
    for f, a in zip(funs[1:], attrs[1:]):
        res.append(getattr(obj, f)(*a))
    print(res)


f = ["Solution", "pick", "pick", "pick"]
s = [[[1, 2, 3, 3, 3]], [3], [1], [3]]
print_func(f, s)
