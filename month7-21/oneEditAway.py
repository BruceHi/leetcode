# 一次编辑
from collections import Counter


class Solution:
    # 要注意顺序
    # def oneEditAway(self, first: str, second: str) -> bool:
    #     if abs(len(first) - len(second)) > 1:
    #         return False
    #
    #     # 长度相同的情况
    #     if first == second:
    #         return True
    #     if len(first) == len(second):
    #         count = 0
    #         for i in range(len(first)):
    #             if first[i] != second[i]:
    #                 count += 1
    #             if count > 1:
    #                 return False
    #         return True
    #
    #     # 长度差 1 的情况
    #     if len(first) < len(second):
    #         first, second = second, first
    #     j = 0
    #     count = 0
    #     for i in range(len(first)):
    #         if j < len(second):
    #             if first[i] == second[j]:
    #                 j += 1
    #             else:
    #                 count += 1
    #             if count > 1:
    #                 return False
    #     return True

    # def oneEditAway(self, first: str, second: str) -> bool:
    #     if len(first) < len(second):
    #         first, second = second, first
    #     k = len(second)
    #     for i, c in enumerate(second):
    #         if c != first[i]:
    #             k = i
    #             break
    #     return first[k+1:] == second[k:] or first[k+1:] == second[k+1:]

    def oneEditAway(self, first: str, second: str) -> bool:
        m, n = len(first), len(second)
        if abs(m-n) > 1:  # 没有这个的话，第二个例子错误
            return False
        for i in range(min(m, n)):
            if first[i] != second[i]:
                return first[i+1:] == second[i:] or first[i+1:] == second[i+1:] or first[i:] == second[i+1:]
        return True


s = Solution()
first = "pale"
second = "ple"
print(s.oneEditAway(first, second))

first = "pales"
second = "pal"
print(s.oneEditAway(first, second))

first = "aaa"
second = "aa"
print(s.oneEditAway(first, second))

first = "aaa"
second = "aaa"
print(s.oneEditAway(first, second))

first = "ab"
second = "bc"
print(s.oneEditAway(first, second))

first = "abc"
second = "bc"
print(s.oneEditAway(first, second))

print(Counter('aa')-Counter('aa') is not True)


