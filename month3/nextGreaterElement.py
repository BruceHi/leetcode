# 496.下一个更大元素1
from typing import List


class Solution:
    # # 常规解法
    # def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     def first_num(a, nums):
    #         for num in nums:
    #             if a < num:
    #                 return num
    #         return -1
    #
    #     res = []
    #     for num in nums1:
    #         res.append(first_num(num, nums2[nums2.index(num):]))
    #     return res

    # 使用栈, dailyTemperatures，时间复杂度 O(M+N)
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic, stack = {}, []
        for num in nums2:
            while stack and num > stack[-1]:
                dic[stack.pop()] = num
            stack.append(num)

        return [dic.get(num, -1) for num in nums1]




s = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(s.nextGreaterElement(nums1, nums2))

nums1 = [2,4]
nums2 = [1,2,3,4]
print(s.nextGreaterElement(nums1, nums2))
