# 503.下一个更大元素 2
from typing import List


class Solution:
    # 常规解法
    # def nextGreaterElements(self, nums: List[int]) -> List[int]:
    #     n = len(nums)
    #     res = []
    #     for i, num in enumerate(nums):
    #         j = (i + 1) % n
    #         flag = 0
    #         while j != i:
    #             if nums[j] > nums[i]:
    #                 res.append(nums[j])
    #                 flag = 1
    #                 break
    #             j = (j + 1) % n
    #         if not flag:
    #             res.append(-1)
    #     return res

    # 使用递减栈，循环数组两次
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2*n - 1):  # 注意减一，第二次的最后一个没有必要算
            while stack and nums[i%n] > nums[stack[-1]]:
                res[stack.pop()] = nums[i%n]
            stack.append(i%n)
        return res


s = Solution()
nums = [1,2,1]
print(s.nextGreaterElements(nums))
