# 除自身以外数组的乘积
from typing import List


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     left, right = [1] * n, [1] * n
    #     res = [0] * n
    #
    #     # 前缀积
    #     for i in range(1, n):
    #         left[i] = left[i-1] * nums[i-1]
    #     # 后缀积
    #     for i in range(n-2, -1, -1):
    #         right[i] = right[i+1] * nums[i+1]
    #
    #     for i in range(n):
    #         res[i] = left[i] * right[i]
    #
    #     return res

    # 若输出数组 res 不被视为额外空间。空间复杂度为 O(1) 的解法。
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 模拟前缀积
        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        r = 1
        for i in range(n-1, -1, -1):
            res[i] = res[i] * r
            r *= nums[i]

        return res


s = Solution()
n = [1,2,3,4]
print(s.productExceptSelf(n))
