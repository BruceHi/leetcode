# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return '1'
#         s = self.countAndSay(n-1)
#
#         count, num, i = 0, 0, 0
#         while i < len(s):
#             j = i
#             while j < len(s) and s[i] == s[j]:  # 不能放反了,否则溢出时会报错
#                 count += 1
#                 j += 1
#             num = num*100 + count*10 + int(s[i])
#             i += count
#             count = 0
#
#         return str(num)
import re

class Solution:
    # def countAndSay(self, n: int) -> str:
    #     if n == 1:
    #         return '1'
    #     s = self.countAndSay(n-1)
    #
    #     i, res = 0, ''  # res代表result.
    #     while i < len(s):
    #         j, count = i, 0
    #         while j < len(s) and s[i] == s[j]:
    #             count += 1
    #             j += 1
    #         res += str(count) + s[i]
    #         i += count
    #
    #     return res

    # # 优化
    # def countAndSay(self, n: int) -> str:
    #     if n == 1:
    #         return '1'
    #     s = self.countAndSay(n-1)
    #
    #     i, res = 0, ''
    #     while i < len(s):
    #         count = 1
    #         while i+1 < len(s) and s[i] == s[i+1]:
    #             count += 1
    #             i += 1
    #         res += str(count) + s[i]
    #         i += 1
    #
    #     return res

    # 改写成循环
    # def countAndSay(self, n: int) -> str:
    #     res = '1'
    #     for _ in range(n-1):
    #         i, tmp = 0, ''
    #         while i < len(res):
    #             count = 1
    #             while i + 1 < len(res) and res[i] == res[i+1]:
    #                 count += 1
    #                 i += 1
    #             tmp += str(count) + res[i]
    #             i += 1
    #         res = tmp
    #
    #     return res


# import re
# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return '1'
#         s = self.countAndSay(n-1)
#
#         p = r'(\d)\1*'
#         pattern = re.compile(p)
#         # strings = [_.group() for _ in pattern.finditer(s)]
#         # # res = ''
#         # # for string in strings:
#         # #     res += str(len(string)) + string[0]
#         # # return res
#         #
#         # return ''.join([str(len(string))+string[0] for string in strings])
#
#         res = [_.group() for _ in pattern.finditer(s)]
#         return ''.join([str(len(_)) + _[0] for _ in res])

    # def countAndSay(self, n: int) -> str:
    #     res = '1'
    #     for _ in range(n-1):
    #         i, tmp = 0, ''
    #         for j, c in enumerate(res):
    #             if c != res[i]:
    #                 tmp += str(j-i) + res[i]
    #                 i = j
    #         res = tmp + str(len(res) - i) + res[-1]
    #     return res

    # def countAndSay(self, n: int) -> str:
    #     if n == 1:
    #         return '1'
    #     s = self.countAndSay(n-1)
    #
    #     i, res = 0, ''
    #     for j, c in enumerate(s):
    #         if c != s[i]:
    #             res += str(j-i) + s[i]
    #             i = j
    #     res += str(len(s) - i) + s[-1]
    #     return res

    # def countAndSay(self, n: int) -> str:
    #     if n == 1:
    #         return '1'
    #     s = self.countAndSay(n-1)
    #
    #     p = r'(\d)\1*'
    #     pattern = re.compile(p)
    #     res = [_.group() for _ in pattern.finditer(s)]
    #     # res = ''.join(str(len(c)) + c[0] for c in str_list)
    #     # print(type(str(len(c)) + c[0] for c in str_list))
    #     return ''.join(str(len(c)) + c[0] for c in res)  # join 内部的 str(len(c)) + c[0] for c in res 表示生成器

    # def countAndSay(self, n: int) -> str:
    #     if n == 1:
    #         return '1'
    #     s = self.countAndSay(n-1)
    #     p = r'(\d)\1*'
    #     pattern = re.compile(p)
    #     res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), s)
    #     return res

    # def countAndSay(self, n: int) -> str:
    #     res = '1'
    #     p = r'(\d)\1*'
    #     pattern = re.compile(p)
    #     for _ in range(n-1):
    #         res = pattern.sub(lambda x: str(len(x.group())) + x.group(1), res)
    #     return res

    # def countAndSay(self, n: int) -> str:
    #     if n == 1:
    #         return '1'
    #     nums = self.countAndSay(n-1)
    #     res = ''
    #     i = 0
    #     for j, num in enumerate(nums):
    #         if num != nums[i]:
    #             res += str(j-i) + nums[i]
    #             i = j
    #     res += str(len(nums)-i) + nums[-1]
    #     return res

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)

        res = ''
        i = 0
        for j, c in enumerate(s):
            if c != s[i]:
                res += str(j-i) + s[i]
                i = j
        res += str(len(s)-i) + s[-1]
        return res


s = Solution()
n = 1
print(s.countAndSay(n))

n = 2
print(s.countAndSay(n))

n = 3
print(s.countAndSay(n))

n = 4
print(s.countAndSay(n))

n = 5
print(s.countAndSay(n))

