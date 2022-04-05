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

    # # 若输出数组 res 不被视为额外空间。空间复杂度为 O(1) 的解法。
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     res = [1] * n
    #
    #     # 模拟前缀积
    #     for i in range(1, n):
    #         res[i] = res[i-1] * nums[i-1]
    #
    #     r = 1
    #     for i in range(n-1, -1, -1):
    #         res[i] = res[i] * r
    #         r *= nums[i]
    #
    #     return res

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     pre, suf = [1] * n, [1] * n
    #
    #     for i in range(1, n):
    #         pre[i] = pre[i-1] * nums[i-1]
    #     for i in range(n-2, -1, -1):
    #         suf[i] = suf[i+1] * nums[i+1]
    #
    #     res = [0] * n
    #     for i in range(n):
    #         res[i] = pre[i] * suf[i]
    #     return res

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     res = [1] * n
    #
    #     for i in range(1, n):
    #         res[i] = res[i-1] * nums[i-1]
    #
    #     r = 1
    #     for i in range(n-1, -1, -1):
    #         res[i] *= r
    #         r *= nums[i]
    #     return res

    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     prefix, suffix = [1], [1]
    #     n = len(nums)
    #
    #     for i in range(1, n):
    #         prefix.append(prefix[-1] * nums[i-1])
    #
    #     for i in range(n-2, -1, -1):
    #         suffix = [suffix[0] * nums[i+1]] + suffix
    #
    #     res = []
    #     for i in range(n):
    #         res.append(prefix[i] * suffix[i])
    #     return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        for i in range(1, n):
            res[i] = res[i-1] * nums[i-1]

        suffix = 1
        for i in range(n-1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res


s = Solution()
nums = [1,2,3,4]
print(s.productExceptSelf(nums))

nums = [-1,1,0,-3,3]
print(s.productExceptSelf(nums))

