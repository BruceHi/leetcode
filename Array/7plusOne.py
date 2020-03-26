# 加一
# list/int/str 相互转换
# def plusOne(digits):
#     # digits = map(str, digits)  # digits是一个迭代器
#     # nums = int(''.join(digits)) + 1  # 转换为整数，并加上1
#     # return list(map(int, str(nums)))  # 数变为单个数字的列表
#
#     return list(map(int, str(int(''.join(map(str, digits))) + 1)))

# from functools import reduce
#
#
# def plusOne(digits):
#     s = reduce((lambda x, y: x * 10 + y), digits) + 1
#     return list(map(int, str(s)))


# 按照加法的进位计算
# def plusOne(digits):
#
#     i = -1
#     digits[i] += 1
#     while digits[i] == 10:
#         digits[i] = 0
#         i -= 1
#         if i < -len(digits):  # 应对出现[9, 9, 9]这样全为9的情况。
#             digits.insert(0, 1)
#             break
#         digits[i] += 1
#
#     return digits

# 按照加法的进位计算，上面的改进
def plusOne(digits):
    i = len(digits) - 1
    while i >= 0:
        digits[i] += 1
        if digits[i] < 10:
            break
        else:  # 需要进位
            digits[i] = 0
            i -= 1
        if i == -1:  # 应对出现[9, 9, 9]这样全为9的情况。
            digits.insert(0, 1)
    return digits


list1 =[9, 9, 9]
print(plusOne(list1))

list1 = [1, 2, 2, 1]
print(plusOne(list1))

list1 =[4,3,2,1]
print(plusOne(list1))