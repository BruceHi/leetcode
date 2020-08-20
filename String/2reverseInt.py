# int --> list --> int：全程操作list
# def reverse(x):
#     nums = list(str(x))
#     k = 0
#     if nums[0] == '-':  # 处理负数
#         nums.pop(0)
#         k = 1
#     nums.reverse()
#
#     x = int(''.join(nums))
#
#     if k:
#         return -x if x <= 2**31 else 0
#     else:
#         return x if x <= 2**31 - 1 else 0


# # int --> string --> int 全程操作string
# def reverse(x):
#     nums_string = str(x)[::-1]  # 先反转，再去掉
#     if nums_string.endswith('-'):
#         return -int(nums_string.rstrip('-')) \
#             if int(nums_string.rstrip('-')) < 2**31 else 0
#     return int(nums_string) if int(nums_string) <= 2**31 - 1 else 0


# # int --> list --> int：全程操作list
# def reverse(x):
#     nums = list(str(x))
#     nums.reverse()
#     if nums[-1] == '-':  # 处理负数
#         nums.pop(-1)
#         return -int(''.join(nums)) if int(''.join(nums)) <= 2**31 else 0
#     return int(''.join(nums)) if int(''.join(nums)) <= 2**31 - 1 else 0


# # int --> string --> int 全程操作string
# def reverse(x):
#     if x >= 0:
#         y = int(str(x)[::-1])
#     else:
#         y = -int(str(x)[:0:-1])
#
#     if y < -2**31 or y > 2**31 - 1:
#         return 0
#     else:
#         return y

# # 数学方法
# def reverse(x):
#     sign = 1 if x > 0 else -1
#     result = 0
#     x = abs(x)
#     while x > 0:
#         result = result * 10 + x % 10
#         x //= 10
#     if -2**31 < sign * result < 2**31 - 1:
#         return sign * result
#     else:
#         return 0

############################################## 下面是第二次做的 #############################
# 转换法
# def reverse(x: int) -> int:
#
#     def change(x):
#         nums = list(str(x))
#         nums.reverse()
#         return int(''.join(nums))
#
#     if x >= 0:
#         if change(x) > 2**31-1:
#             return 0
#         return change(x)
#
#     if -change(-x) < -2**31:
#         return 0
#     return -change(-x)

# def reverse(x: int) -> int:
#     if x >= 0:
#         y = int(str(x)[::-1])
#     else:
#         y = -int(str(-x)[::-1])
#
#     if -2**31 <= y <= 2**31-1:
#         return y
#     return 0

# 数学法，python 中的求余是根据整除而算出来的，整除都是向下取整。
# 所以负数的求余求整，跟我们日常所理解的不同。
# 下面方法针对负数，没效果。
# def reverse(x: int) -> int:
#     int_max, int_min = 2**31-1, -2**31
#     res = 0
#     while x:
#         res = res * 10 + x % 10
#         x //= 10
#         if res > int_max // 10 or res == int_max // 10 and x % 10 > 7:
#             return 0
#         if res < int_min // 10 or res == int_min // 10 and x % 10 < -8:
#             return 0
#     return res

# def reverse(x: int) -> int:
#     if x >= 0:
#         sign = 1
#     else:
#         sign, x = -1, -x
#
#     res = 0
#     while x:
#         res = res * 10 + x % 10
#         x //= 10
#
#     if -2**31 <= sign * res <= 2**31-1:
#         return sign * res
#     return 0

# # 字符串转换
def reverse(x: int) -> int:
    sign = 1 if x > 0 else -1
    x = x if x > 0 else -x
    res = sign * int(str(x)[::-1])
    if - 2 ** 31 < res < 2 ** 31 - 1:
        return res
    return 0

# # 数学方法
# def reverse(x: int) -> int:
#     sign = 1 if x > 0 else -1
#     n = x if x > 0 else -x
#     res = 0
#     while n:
#         res = res * 10 + n % 10
#         n //= 10
#     res = sign * res
#     if - 2 ** 31 < res < 2 ** 31 - 1:
#         return res
#     return 0



a = -123
print(reverse(a))

a = 120
print(reverse(a))

a = 123
print(reverse(a))

a = 1534236469
print(reverse(a))
