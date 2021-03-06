# 179. 最大数
# python3.9 使用 list 代替 from typing import List，其他版本的不行
from functools import cmp_to_key


class Solution:
    # 错误
    # def largestNumber(self, nums: list[int]) -> str:
    #     nums_str = [str(num) for num in nums]
    #     n = max(len(c) for c in nums_str)
    #     # print(n)
    #     nums_str.sort(key=lambda x: x + (n - len(x)) * x[-1], reverse=True)
    #     # a = list(map(lambda x: x + (n - len(x)) * x[-1], nums_str))
    #     # print(a)
    #     # print(nums_str)
    #     return ''.join(nums_str)

    # 错误
    # def largestNumber(self, nums: list[int]) -> str:
    #     nums_str = [str(num) for num in nums]
    #     n = max(len(c) for c in nums_str)
    #     nums_str.sort(key=lambda x: x + (n - len(x)) * x[-1], reverse=True)
    #     return ''.join(nums_str)

    # def largestNumber(self, nums: list[int]) -> str:
    #     # 全部都是 0
    #     if not any(nums):
    #         return '0'
    #     res = ''.join(sorted(map(str, nums), key=Larger))
    #     return res

    # https://docs.python.org/zh-cn/3.7/howto/sorting.html#sortinghowto
    # 接受两个参数进行对比，使用 cmp_to_key。在 python 2 中不用 cmp_to_key 可以直接比较。
    def largestNumber(self, nums: list[int]) -> str:
        # 全部都是 0
        if not any(nums):
            return '0'
        # 在cmp 中，返回负数为小于，返回正数为大于，返回 0 为相等。x 写在前的返回小于号。
        cmp = lambda x, y: int(x+y) - int(y+x)
        res = ''.join(sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True))
        return res


# class Larger(str):
#     def __lt__(x, y):
#         return x+y > y+x


s = Solution()
nums = [10,2]
print(s.largestNumber(nums))

nums = [3,30,34,5,9]
print(s.largestNumber(nums))

nums = [1]
print(s.largestNumber(nums))

nums = [10]
print(s.largestNumber(nums))

nums = [34323,3432]
print(s.largestNumber(nums))

nums = [0, 0]
print(s.largestNumber(nums))
