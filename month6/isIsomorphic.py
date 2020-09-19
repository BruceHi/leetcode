# 同构字符串
class Solution:

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     dic = {}
    #     for i in range(len(s)):
    #         if s[i] not in dic:
    #             if t[i] in dic.values():  # s = "ab" t = "cc"
    #                 return False
    #             dic[s[i]] = t[i]
    #         else:
    #             if dic[s[i]] != t[i]:
    #                 return False
    #     return True
    #
    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     dic = {}
    #     for a, b in zip(s, t):
    #         if a not in dic:
    #             if b in dic.values():
    #                 return False
    #             dic[a] = b
    #         else:
    #             if dic[a] != b:
    #                 return False
    #     return True

    # def isIsomorphic(self, s: str, t: str) -> bool:
    #     record = {}
    #     for i in range(len(s)):
    #         if s[i] not in record:
    #             if t[i] in record.values():
    #                 return False
    #             record[s[i]] = t[i]
    #         elif record[s[i]] != t[i]:
    #             return False
    #     return True

    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for a, b in zip(s, t):
            if a not in dic:
                if b in dic.values():
                    return False
                dic[a] = b
            elif dic[a] != b:
                return False
        return True


obj = Solution()
s = "egg"
t = "add"
print(obj.isIsomorphic(s, t))

s = "foo"
t = "bar"
print(obj.isIsomorphic(s, t))

s = "paper"
t = "title"
print(obj.isIsomorphic(s, t))

s = "ab"
t = "aa"
print(obj.isIsomorphic(s, t))

s = "bb"
t = "ac"
print(obj.isIsomorphic(s, t))