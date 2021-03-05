# 303. 区域和检索 - 数组不可变
from typing import List
from operator import add


# class NumArray:
#
#     def __init__(self, nums: List[int]):
#         self.nums = nums
#
#     def sumRange(self, i: int, j: int) -> int:
#         return sum(self.nums[i:j+1])

# 使用前缀和
class NumArray:

    # def __init__(self, nums: List[int]):
    #     n = len(nums)
    #     self.pre = [0] * (n+1)
    #     for i in range(1, n+1):
    #         self.pre[i] = self.pre[i-1] + nums[i-1]
    #
    #
    # def sumRange(self, i: int, j: int) -> int:
    #     return self.pre[j+1] - self.pre[i]

    def __init__(self, nums: List[int]):
        self.pre_num = [0]
        for num in nums:
            self.pre_num.append(self.pre_num[-1] + num)


    def sumRange(self, i: int, j: int) -> int:
        return self.pre_num[j+1] - self.pre_num[i]


s = NumArray([-2, 0, 3, -5, 2, -1])
print(s.sumRange(0, 2))
print(s.sumRange(2, 5))
print(s.sumRange(0, 5))


# # * 表示解包
# def function(function, args):
#     res = []
#     for fun, args in zip(function, args):
#         res.append(fun(*args))
#     return res
#
# a = function([sum, add], [[[1, 2]], [2, 3]])
# print(a)

# a = function(NumArray, [[-2, 0, 3, -5, 2, -1]])
# print(a)

# 调用失败
# def func2(funs, args):
#     res = [funs[0](*args[0])]
#     for fun, arg in zip(funs[1:], args[1:]):
#         # print(fun)
#         # fun = globals().get(fun)
#         # print(fun)
#         res.append(res[0].fun(*arg))
#     return res
#
#
# # fun = globals().get('')
#
# funs = [NumArray, 'sumRange', 'sumRange', 'sumRange']
# args = [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# print(func2(funs, args))

