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

# 数学方法
def reverse(x):
    sign = 1 if x > 0 else -1
    result = 0
    x = abs(x)
    while x > 0:
        result = result * 10 + x % 10
        x //= 10
    if -2**31 < sign * result < 2**31 - 1:
        return sign * result
    else:
        return 0


a = -123
print(reverse(a))

a = 120
print(reverse(a))

a = 123
print(reverse(a))

a = 1534236469
print(reverse(a))
