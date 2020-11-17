# 移动石子，该题很坑。
# 结束时的状态应该是三个数连在一起的。

#
# 最小数: 1
# 1 55 56   ->   54 55 56
# 1 3 56    ->   1 2 3

# 其它的最小数: 2
# eg: 1 23 55  ->  22 23 24 或 1 2 3（55——>2, 23-->3） 或 53 54 55(1-->54, 23-->53)


# def numMovesStones(a, b, c):
#     nums = [a, b, c]
#     nums.sort()
#     x, y = nums[1] - nums[0] - 1, nums[2] - nums[1] - 1
#     max = x + y
#     min = 0
#     if x != 0 or y != 0:
#         if x > 1 and y > 1:
#             min = 2
#         else:
#             min = 1
#     return [min, max]

from typing import List


class Solution:
    # def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
    #     a, b, c = sorted([a, b, c])
    #     x, y = b - a - 1, c - b - 1
    #     if not x and not y:  # 两个为空
    #         return [0, 0]
    #     if not x or not y:  # 有一个为空
    #         return [1, x+y]
    #     if x == 1 or y == 1:  # 有一个为 1
    #         return [1, x+y]
    #     return [2, x+y]  # 都不为空

    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        a, b, c = sorted([a, b, c])
        x, y = b - a - 1, c - b - 1
        min_v, max_v = 0, x + y

        if x or y:  # 至少有一个不为 0
            if x > 1 and y > 1:
                min_v = 2
            else:
                min_v = 1
        return [min_v, max_v]


s = Solution()
a = 1
b = 2
c = 5
print(s.numMovesStones(a, b, c))

a = 4
b = 3
c = 2
print(s.numMovesStones(a, b, c))

a = 3
b = 5
c = 1
print(s.numMovesStones(a, b, c))  # (1, 2)

print(s.numMovesStones(7, 4, 1))

