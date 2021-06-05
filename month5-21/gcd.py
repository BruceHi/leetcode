# 辗转相除法
# 递归
def gcd(x, y):
    return x if y == 0 else gcd(y, x % y)  # y 是较小的那个值


print(gcd(378, 5940))
print(gcd(5940, 378))


# 迭代
def gcd(x, y):
    # if y > x:
    #     x, y = y, x
    # while y != 0:
    #     x, y = y, x % y
    # return x
    while y:
        x, y = y, x % y
    return x


print(gcd(378, 5940))
print(gcd(5940, 378))

print(gcd(3, 7))


# 普通遍历
def gcd(x, y):
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i


print(gcd(378, 5940))
print(gcd(5940, 378))

print(gcd(3, 7))
