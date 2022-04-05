import re


# # 正则表达式
# def myAtoi(str):
#     p = r'^\s*[+-]?\d+'
#     pattern = re.compile(p)
#     str_list = pattern.findall(str)
#     num = int(*str_list)  # int()为 0

#     if not num:
#         return 0
#     if num > 0:
#         return min(num, 2**31 - 1)
#     return max(num, -2**31)


# def myAtoi(str):
#     return max(min(int(*re.findall(r'^[+-]?\d+', str.lstrip())), 2**31 - 1), -2**31)
#     # return max(min(int(*re.findall(re.compile(r'^\s*[+-]?\d+'), str)), 2**31 - 1), -2**31)

# def myAtoi(str):
#     p = r'^\s*[-+]?\d+'
#     pattern = re.compile(p)
#     num_str = pattern.findall(str)
#     num = ''.join(num_str)

#     if not num:
#         return 0
#     if int(num) < -2 ** 31:
#         return -2 ** 31
#     if int(num) > 2 ** 31 - 1:
#         return 2 ** 31 - 1
#     return int(num)


# def myAtoi(str: str) -> int:
#     p = r'^\s*[+-]?\d+'
#     pattern = re.compile(p)
#     res_list = pattern.findall(str)
#     res = int(*res_list)
#
#     if res < -2**31:
#         return -2**31
#     if res > 2**31 - 1:
#         return 2**31 - 1
#     return res

# def myAtoi(s: str) -> int:
#     p = r'\s*[+-]?\d+'
#     p = re.compile(p)
#     res = p.match(s)
#     if res:
#         num = int(res.group())
#         if num < -2**31:
#             return -2**31
#         if num > 2**31-1:
#             return 2**31-1
#         return num
#     else:
#         return 0


# def myAtoi(s: str) -> int:
#     p = r'^\s*[+-]?\d+'
#     pattern = re.compile(p)
#     res = pattern.match(s)
#
#     if res:
#         num = int(res.group())
#         if num < -2**31:
#             return -2**31
#         if num > 2**31-1:
#             return 2**31-1
#         return num
#     else:
#         return 0

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        p = r'^[-+]?\d+'
        p = re.compile(p)
        res = p.match(s)
        if res:
            num = int(res.group())
            if num < -2 ** 31:
                return -2 ** 31
            if num > 2 ** 31 - 1:
                return 2 ** 31 - 1
            return num
        return 0

    # def myAtoi(self, str):
    #     p = r'^\s*[-+]?\d+'
    #     pattern = re.compile(p)
    #     num_str = pattern.findall(str)
    #     print(num_str)
    #     num = ''.join(num_str)
    #     print(num)

obj = Solution()
s = " "
print(obj.myAtoi(s))

s = "+1"
print(obj.myAtoi(s))

s = ""
print(obj.myAtoi(s))

s = "   2-4c2"
print(obj.myAtoi(s))

s = "   -4c2"
print(obj.myAtoi(s))

s = "+-12"
print(obj.myAtoi(s))

s = "   -42"
print(obj.myAtoi(s))

s = "42"
print(obj.myAtoi(s))

s = "4193 with words"
print(obj.myAtoi(s))

s = "words and 987"
print(obj.myAtoi(s))

s = "ab"
print(obj.myAtoi(s))

# 溢出判断
s = "-91283472332"
print(obj.myAtoi(s))


s = "2147483648"
print(obj.myAtoi(s))

s = "-2147483649"
print(obj.myAtoi(s))

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

