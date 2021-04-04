# 42. 接雨水
# 与 largestRectangleArea 相似
from typing import List


class Solution:
    # 构建递减（包括相同的）栈，遇见大的就弹出去
    # def trap(self, height: List[int]) -> int:
    #     res, stack = 0, []
    #     for i, num in enumerate(height):
    #         while stack and num > height[stack[-1]]:
    #             idx = stack.pop()
    #             if stack:
    #                 h = min(height[stack[-1]], num) - height[idx]
    #                 res += (i-stack[-1]-1) * h
    #         stack.append(i)
    #     return res

    def trap(self, height: List[int]) -> int:
        res = 0
        stack = []
        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                val = height[stack.pop()]
                if stack:
                    res += (i-stack[-1]-1) * (min(height[stack[-1]], h) - val)
            stack.append(i)
        return res


s = Solution()
height = [1, 0, 2]
print(s.trap(height))

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(s.trap(height))

height = [4,2,0,3,2,5]
print(s.trap(height))

height = []
print(s.trap(height))

height = [1, 2, 3, 4]
print(s.trap(height))
