# 验证回文字符串
# 双指针
# def isPalindrome(s):
#
#     def alpha_and_num(char):
#         return char.isalnum()
#
#     def up_to_low(string):
#         return string.lower()
#
#     s = list(map(up_to_low, filter(alpha_and_num, s)))  # 过滤掉非字母数字的,然后字母都转为小写的。
#
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] != s[right]:
#             return False
#         left, right = left + 1, right - 1
#     return True


# # 双指针 改进
# def isPalindrome(s):
#     s = list(filter(str.isalnum, s.lower()))
#     return s == s[::-1]


# # 双指针 改进
# def isPalindrome(s):
#     s = list(map(str.lower, filter(str.isalnum, s)))
#     return s == s[::-1]


# 不整理数据，直接进行双指针的移动
# def isPalindrome(s):
#
#     left, right = 0, len(s) - 1
#     while left < right:
#         while not s[left].isalnum() and left < right:  # 寻找下一个字母或数字点。加上left < right，怎么遍历也不会越界。
#             left += 1
#         while not s[right].isalnum() and left < right:  # 若没找到，最终形成left与right只差一个单位。然后再进行一步退出循环。
#             right -= 1
#         if s[left].lower() != s[right].lower():
#             return False
#         left, right = left + 1, right - 1
#
#     return True


def isPalindrome(s):
    left, right = 0, len(s)-1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left, right = left + 1, right - 1
    return True


s = "a."
print(isPalindrome(s))

s = ".,"
print(isPalindrome(s))

s = "A man, a plan, a canal: Panama"

print(isPalindrome(s))

s = "123ec321"
print(isPalindrome(s))

s = "race a car"
print(isPalindrome(s))


