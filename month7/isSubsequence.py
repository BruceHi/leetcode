# 判断子序列
class Solution:
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     m, n = len(s), len(t)
    #     if not m:
    #         return True
    #     i = j = 0
    #     while j < n:
    #         if s[i] == t[j]:
    #             i += 1
    #         j += 1
    #         if i == m:
    #             return True
    #     return False

    # def isSubsequence(self, s: str, t: str) -> bool:
    #     m, n = len(s), len(t)
    #     i = j = 0
    #     while i < m and j < n:
    #         if s[i] == t[j]:
    #             i += 1
    #         j += 1
    #     return i == m

    # def isSubsequence(self, s: str, t: str) -> bool:
    #     if not s:
    #         return True
    #     i = 0
    #     for c in t:
    #         if c == s[i]:
    #             i += 1
    #             if i == len(s):
    #                 return True
    #     return False

    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i = j = 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == m


obj = Solution()
s = "abc"
t = "ahbgdc"
print(obj.isSubsequence(s, t))

s = "axc"
t = "ahbgdc"
print(obj.isSubsequence(s, t))

s = ""
t = "ahbgdc"
print(obj.isSubsequence(s, t))

s = "b"
t = "abc"
print(obj.isSubsequence(s, t))
