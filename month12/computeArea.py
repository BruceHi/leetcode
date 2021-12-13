# 223. 矩形面积
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area1 = (ax2 - ax1) * (ay2 - ay1)
        area2 = (bx2 - bx1) * (by2 - by1)
        overlap_x = min(ax2, bx2) - max(ax1, bx1)
        overlap_y = min(ay2, by2) - max(ay1, by1)
        overlap_area = max(overlap_x, 0) * max(overlap_y, 0)
        return area1 + area2 - overlap_area


s = Solution()
ax1 = -3
ay1 = 0
ax2 = 3
ay2 = 4
bx1 = 0
by1 = -1
bx2 = 9
by2 = 2
print(s.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))

ax1 = -2
ay1 = -2
ax2 = 2
ay2 = 2
bx1 = -2
by1 = -2
bx2 = 2
by2 = 2
print(s.computeArea(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2))
