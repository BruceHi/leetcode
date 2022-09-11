# 396. 旋转函数
from typing import List


class Solution:
    # 找出 f(k) 与 f(k-1) 之间的关系
    # 公式推导
    # F(k)=F(k−1)+numSum−n×nums[n−k]
    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     sum_nums = sum(nums)
    #     f = 0
    #     for i, num in enumerate(nums):
    #         f += i * num
    #     res = f
    #
    #     n = len(nums)
    #     for i in range(1, n):
    #         f += sum_nums - n * nums[n-i]
    #         res = max(res, f)
    #     return res

    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     f = 0
    #     for i, num in enumerate(nums):
    #         f += i * num
    #
    #     res = f
    #     sum_nums = sum(nums)
    #     n = len(nums)
    #     for i in range(1, n):
    #         f += sum_nums - n * nums[n-i]
    #         res = max(res, f)
    #     return res

    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     f = 0
    #     for i, num in enumerate(nums):
    #         f += i * num
    #
    #     sum_nums = sum(nums)
    #     res = f
    #     n = len(nums)
    #     for i in range(1, n):
    #         f += sum_nums - n * nums[n-i]
    #         res = max(res, f)
    #     return res


    # 思路
    # 列出 f(0) 的式子，f(1) 的式子，再找出f(1) 与 f(0) 的关系，进而进行替换，写出 f(k) 与 f(k-1) 的关系
    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     f = 0
    #     for i, num in enumerate(nums):
    #         f += i * num
    #
    #     res = f
    #     n = len(nums)
    #     sum_nums = sum(nums)
    #     for i in range(1, n):
    #         f += sum_nums - n * nums[n-i]
    #         res = max(res, f)
    #     return res

    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     sum_num = sum(nums)
    #     count = 0
    #     for i, num in enumerate(nums):
    #         count += i * num
    #     res = count
    #
    #     n = len(nums)
    #     for i in range(1, n):
    #         count += sum_num - n * nums[n - i]
    #         res = max(res, count)
    #     return res

    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     f = 0
    #     for i, num in enumerate(nums):
    #         f += i * num
    #     res = f
    #
    #     sum_nums = sum(nums)
    #     n = len(nums)
    #     for i in range(1, n):
    #         f += sum_nums - n * nums[n - i]
    #         res = max(res, f)
    #     return res


    # def maxRotateFunction(self, nums: List[int]) -> int:
    #     f = 0
    #     for i, num in enumerate(nums):
    #         f += i * num
    #
    #     res = f
    #     n = len(nums)
    #     sum_nums = sum(nums)
    #     for i in range(1, n):
    #         f += sum_nums - n * nums[n-i]
    #         res = max(res, f)
    #     return res

    def maxRotateFunction(self, nums: List[int]) -> int:
        f = 0
        for i, num in enumerate(nums):
            f += i * num

        res = f
        sum_nums = sum(nums)
        n = len(nums)
        for i in range(1, n):
            f += sum_nums - n * nums[n-i]
            res = max(res, f)
        return res


s = Solution()
nums = [4,3,2,6]
print(s.maxRotateFunction(nums))

nums = [100]
print(s.maxRotateFunction(nums))

nums = [1,2,3,4,5,6,7,8,9,10]
print(s.maxRotateFunction(nums))
