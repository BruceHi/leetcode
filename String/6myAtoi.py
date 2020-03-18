# def myAtoi(str):
#     str.lstrip('')
#     str.isdigit()
#     y = 0
#     for i in range(len(str)):
#         if str[i].isdigit() and not str[i+1].isdigit():
#             y = y*10 + int(str[i])
#         elif str[i] == '-':
#             pass
#         else:
#             return False
#
#     return y


# 双指针
# def myAtoi(str):
#     INT_MAX = 2**31 - 1
#     INT_MIN = -2**31
#     str = str.strip(' ')
#     if len(str) == 0:
#         return 0
#     if str[0] != '-' and not str[0].isdigit() and str[0] != '+':
#             return 0
#
#     if len(str) == 1 and (str[0] == '-' or str[0] == '+'):  # 长度为1，且为‘-’
#         return 0
#     temp = list(str[0])
#     for i in range(1, len(str)):
#         if str[i].isdigit():
#             temp.append(str[i])
#         else:
#             break
#
#     if str[0] == '-':
#         y = -int(''.join(temp[1:]))
#         return y if y.bit_length() <= 32 else INT_MIN
#     elif str[0] == '+':
#         y = int(''.join(temp[1:]))
#         return y if y.bit_length() <= 32 else INT_MAX
#     else:
#         y = int(''.join(temp))
#         return y if y.bit_length() <= 32 else INT_MAX

import re


# 正则表达式
# def myAtoi(str):
#     INT_MAX = 2**31 - 1
#     INT_MIN = -2**31
#     p = r'^\s*([+-]?\d+)'
#     pattern = re.compile(p)
#     str_list = pattern.findall(str)
#     num = int(*str_list)  # int()为0
#     if num > 0:
#         return min(num, INT_MAX)
#     elif num == 0:
#         return 0
#     else:
#         return max(num, INT_MIN)


def myAtoi(str):
    return max(min(int(*re.findall(r'^[+-]?\d+', str.lstrip())), 2**31 - 1), -2**31)
    # return max(min(int(*re.findall(re.compile(r'^\s*([+\-]?\d+)'), str)), 2**31 - 1), -2**31)


s = " "

print(myAtoi(s))

s = "+1"
print(myAtoi(s))

s = ""
print(myAtoi(s))

s = "   2-4c2"
print(myAtoi(s))

s = "   -4c2"
print(myAtoi(s))

s = "   -42"
print(myAtoi(s))

s = "42"
print(myAtoi(s))

s = "4193 with words"
print(myAtoi(s))

s = "words and 987"
print(myAtoi(s))

s = "-91283472332"
print(myAtoi(s))

s = "ab"
print(myAtoi(s))

# 溢出判断
s = "2147483648"
print(myAtoi(s))

s = "-2147483649"
print(myAtoi(s))

# # 其他
# a = -2147483649
# print(a.bit_length())
# print(bin(a))
#
# a = 0b10000000000000000000000000000001
# print(a.bit_length())
#
# b = -129
# print(b.bit_length())
#
# a = 8
# print(a.bit_length())
#
# a = -8
# print(a.bit_length())
#
# print()

print(int())
