# 179. 最大数
# python3.9 使用 list 代替 from typing import List，其他版本的不行
from functools import cmp_to_key
from typing import List


class Solution:
    # def largestNumber(self, nums: list[int]) -> str:
    #     # 全部都是 0
    #     if not any(nums):
    #         return '0'
    #     res = ''.join(sorted(map(str, nums), key=Larger))
    #     return res

    # https://docs.python.org/zh-cn/3.7/howto/sorting.html#sortinghowto
    # 接受两个参数进行对比，使用 cmp_to_key。在 python 2 中不用 cmp_to_key 可以直接比较。
    # def largestNumber(self, nums: list[int]) -> str:
    #     # 全部都是 0
    #     if not any(nums):
    #         return '0'
    #     # 在cmp 中，返回负数为小于，返回正数为大于，返回 0 为相等。
    #
    #     cmp x，写在前由小增大
    #     cmp = lambda x, y: int(x+y) - int(y+x)
    #     res = ''.join(sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True))
    #     return res


# class Larger(str):
#     def __lt__(x, y):
#         return x+y > y+x

    # def largestNumber(self, nums: List[int]) -> str:
    #     # >= 1个数为 0，反面 所有数为0
    #     if not any(nums):
    #         return '0'
    #
    #     cmp = lambda x, y: int(x+y) - int(y+x)
    #     return ''.join(sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True))

    def largestNumber(self, nums: List[int]) -> str:
        # 至少 1 个 1，反面：全部为 0
        if not any(nums):
            return '0'
        cmp = lambda x, y: int(x+y) - int(y+x)
        return ''.join(sorted(map(str, nums), key=cmp_to_key(cmp), reverse=True))


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

nums = [1, 0]
print(s.largestNumber(nums))
