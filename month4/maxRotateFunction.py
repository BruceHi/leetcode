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
