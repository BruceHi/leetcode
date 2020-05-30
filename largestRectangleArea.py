# 柱状图中最大的矩形
from typing import List


class Solution:
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     stack, res = [], 0
    #     for h in heights:
    #         while stack and stack[-1] > h:
    #             stack.pop()
    #         if not stack:
    #             res = max(res, h)
    #         for i, v in enumerate(stack):
    #             res = max(res, v * (len(stack)-i+1), h)
    #         stack.append(h)
    #
    #     return res

    # # 暴力法
    # def largestRectangleArea(self, heights: List[int]) -> int:
    #     res, n = 0, len(heights)
    #     for i, val in enumerate(heights):
    #         left, right = i, i
    #         while left >= 0 and heights[left] >= val:
    #             left -= 1
    #         while right < n and val <= heights[right]:
    #             right += 1
    #         res = max(res, val * (right-left-1))
    #     return res

    # 栈：里面放的是单调递增(单调非递减)数据的索引
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, stack = 0, []
        heights = [0] + heights + [0]
        for i, val in enumerate(heights):
            while stack and heights[stack[-1]] > val:
                tmp = stack.pop()
                res = max(res, (i-stack[-1]-1) * heights[tmp])
            stack.append(i)
        return res


s = Solution()
nums = [2,1,5,6,2,3]
print(s.largestRectangleArea(nums))

nums = [1]
print(s.largestRectangleArea(nums))

nums = [1, 1]
print(s.largestRectangleArea(nums))

nums = [0, 9]
print(s.largestRectangleArea(nums))

nums = [2,1,2]
print(s.largestRectangleArea(nums))

