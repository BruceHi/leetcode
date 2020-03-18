# 盛最多水的容器
def maxArea(height):
    left = 0
    right = len(height) - 1
    area = 0
    while left < right:  # 低的移动，木桶盛水多少取决于最短的那个
        if height[left] >= height[right]:
            area = max(area, height[right] * (right-left))
            right -= 1
        else:
            area = max(area, height[left] * (right - left))
            left += 1
    return area


h = [1,8,6,2,5,4,8,3,7]
print(maxArea(h))
