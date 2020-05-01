# 移动石子，该题很坑。
# 结束时的状态应该是三个数连在一起的。

#
# 最小数: 1
# 1 55 56   ->   54 55 56
# 1 3 56    ->   1 2 3

# 其它的最小数: 2
# eg: 1 23 55  ->  22 23 24 或 1 2 3（55——>2, 23-->3） 或 53 54 55(1-->54, 23-->53)


def numMovesStones(a, b, c):
    nums = [a, b, c]
    nums.sort()
    x, y = nums[1] - nums[0] - 1, nums[2] - nums[1] - 1
    max = x + y
    min = 0
    if x != 0 or y != 0:
        if x > 1 and y > 1:
            min = 2
        else:
            min = 1
    return [min, max]


a = 3
b = 5
c = 1
print(numMovesStones(a, b, c))

a = 1
b = 2
c = 5
print(numMovesStones(a, b, c))

a = 4
b = 3
c = 2
print(numMovesStones(a, b, c))
