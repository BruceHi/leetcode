# 盛最多水的容器
# def maxArea(height):
#     left = 0
#     right = len(height) - 1
#     area = 0
#     while left < right:  # 低的移动，木桶盛水多少取决于最短的那个
#         if height[left] >= height[right]:
#             area = max(area, height[right] * (right-left))
#             right -= 1
#         else:
#             area = max(area, height[left] * (right - left))
#             left += 1
#     return area

from typing import List


# def maxArea(height: List[int]) -> int:
#     left, right = 0, len(height) - 1
#     res = 0
#     while left < right:
#         if height[left] < height[right]:
#             area = (right - left) * height[left]
#             left += 1
#         else:
#             area = (right - left) * height[right]
#             right -= 1
#         res = max(area, res)
#     return res

# def maxArea(height: List[int]) -> int:
#     left, right = 0, len(height) - 1
#     res = 0
#     while left < right:
#         area = (right - left) * min(height[left], height[right])
#         res = max(area, res)
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     return res

# def maxArea(height: List[int]) -> int:
#     left, right = 0, len(height) - 1
#     res = 0
#     while left < right:
#         res = max(res, (right-left)*min(height[left], height[right]))
#         if height[left] < height[right]:
#             left += 1
#         else:
#             right -= 1
#     return res

def maxArea(height: List[int]) -> int:
    res = float('-inf')
    left, right = 0, len(height)-1
    while left < right:
        res = max(res, (right-left)*min(height[left], height[right]))
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res


h = [1,8,6,2,5,4,8,3,7]
print(maxArea(h))

h = [1,8]
print(maxArea(h))