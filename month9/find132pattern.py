# 456.123 模式
from typing import List


class Solution:
    # 错误
    # def find132pattern(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     if n < 3:
    #         return False
    #     for i in range(1, n-1):
    #         if nums[i-1] < nums[i+1] < nums[i]:
    #             return True
    #         if nums[i] == nums[i+1]:
    #             nums[i] = nums[i-1]
    #     return False

    # 贪心法
    # 暴力法，遍历 3， 维护一个最小值，然后遍历 2
    # 超时
    # def find132pattern(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     min_i = nums[0]
    #     for j in range(1, n-1):
    #         for k in range(j+1, n):
    #             if min_i < nums[k] < nums[j]:
    #                 return True
    #         min_i = min(min_i, nums[j])
    #     return False

    # 递减栈，比 nums[j]元素小的都弹了出去，所以是递减栈
    # numsk 是比 nums[j]小的最大元素
    # leftmin 是1， stack（numsk） 是 2， nums[j]是 3
    # def find132pattern(self, nums: List[int]) -> bool:
    #     n = len(nums)
    #     leftmin = [float('inf')] * n
    #     for i in range(1, n):
    #         leftmin[i] = min(leftmin[i-1], nums[i-1])
    #
    #     stack = []
    #     for j in range(n-1, -1, -1):
    #         numsk = float('-inf')
    #         while stack and stack[-1] < nums[j]:
    #             numsk = stack.pop()
    #         if leftmin[j] < numsk:
    #             return True
    #         stack.append(nums[j])
    #
    #     return False

    # 单调栈，k是小于 nums[i] 的最大值。
    # stack 维护的是 3， k 是 2，供下次使用，遍历的是 1。
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        k = float('-inf')
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < k:
                return True
            while stack and stack[-1] < nums[i]:
                k = max(k, stack.pop())
            stack.append(nums[i])
        return False


s = Solution()
nums = [1,2,3,4]
print(s.find132pattern(nums))

nums = [3,1,4,2]
print(s.find132pattern(nums))

nums = [-1,3,2,0]
print(s.find132pattern(nums))

# 平台
nums = [1,3,3,2]
print(s.find132pattern(nums))

nums = [1,0,1,-4,-3]
print(s.find132pattern(nums))

nums = [3, 5, 0, 3, 4]
print(s.find132pattern(nums))
