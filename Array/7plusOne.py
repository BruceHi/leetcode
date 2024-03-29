# 加一
# list/int/str 相互转换
# def plusOne(digits):
#     # digits = map(str, digits)  # digits是一个迭代器
#     # nums = int(''.join(digits)) + 1  # 转换为整数，并加上1
#     # return list(map(int, str(nums)))  # 数变为单个数字的列表
#
#     return list(map(int, str(int(''.join(map(str, digits))) + 1)))

# from functools import reduce
# #
# #
# def plusOne(digits):
#     s = reduce((lambda x, y: x * 10 + y), digits) + 1
#     print(s)
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
# def plusOne(digits):
#     i = len(digits) - 1
#     while i >= 0:
#         digits[i] += 1
#         if digits[i] < 10:
#             break
#         else:  # 需要进位
#             digits[i] = 0
#             i -= 1
#         if i == -1:  # 应对出现[9, 9, 9]这样全为9的情况。
#             digits.insert(0, 1)
#     return digits

from typing import List


# def plusOne(digits: List[int]) -> List[int]:
#     i = len(digits) - 1
#     while i >= 0:
#         digits[i] += 1
#         if digits[i] < 10:
#             break
#         else:
#             digits[i] = 0
#             i -= 1
#     if i == -1:
#         digits.insert(0, 1)
#     return digits


# def plusOne(digits: List[int]) -> List[int]:
#     i = len(digits) - 1
#     while i >= 0:
#         digits[i] += 1
#         if digits[i] < 10:
#             return digits
#         else:
#             digits[i] = 0
#             i -= 1
#     digits.insert(0, 1)
#     return digits


# 由于每次加上 1，所以最大结果是 10
# def plusOne(digits: List[int]) -> List[int]:
#     for i in range(len(digits) - 1, -1, -1):
#         digits[i] += 1
#         if digits[i] < 10:
#             return digits
#         else:
#             digits[i] = 0
#     return [1] + digits

# def plusOne(digits: List[int]) -> List[int]:
#     carry = 1
#     for i in range(len(digits) - 1, -1, -1):
#         re = (digits[i] + carry) % 10
#         carry = (digits[i] + carry) // 10
#         digits[i] = re
#         if not carry:
#             return digits
#     return [1] + digits

# def plusOne(digits: List[int]) -> List[int]:
#     carry = 1
#     res = []
#     for d in digits[::-1]:
#         num = d + carry
#         res = [num%10] + res
#         carry = num // 10
#     if carry:
#         res = [1] + res
#     return res

# def plusOne(digits: List[int]) -> List[int]:
#     for i in range(len(digits)-1, -1, -1):
#         digits[i] += 1
#         digits[i] %= 10
#         if digits[i]:
#             return digits
#     return [1] + digits


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] < 10:
                return digits
            digits[i] = 0
        return [1] + digits


s = Solution()
list1 =[9, 9, 9]
print(s.plusOne(list1))

list1 = [1, 2, 2, 1]
print(s.plusOne(list1))

list1 =[4,3,2,1]
print(s.plusOne(list1))

list1 =[0]
print(s.plusOne(list1))
