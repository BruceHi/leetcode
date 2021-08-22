# 面试题 01.09. 字符串轮转
class Solution:
    # def isFlipedString(self, s1: str, s2: str) -> bool:
    #     if len(s1) != len(s2):
    #         return False
    #     if not s1:
    #         return True
    #     for i in range(len(s1)):
    #         if s1[i:] + s1[:i] == s2:
    #             return True
    #     return False

    # def isFlipedString(self, s1: str, s2: str) -> bool:
    #     if len(s1) != len(s2):
    #         return False
    #     return s2 in s1 + s1

    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and s2 in s1 + s1

s = Solution()
s1 = "waterbottle"
s2 = "erbottlewat"
print(s.isFlipedString(s1, s2))

s1 = "aa"
s2 = "aba"
print(s.isFlipedString(s1, s2))

s1 = ""
s2 = ""
print(s.isFlipedString(s1, s2))
