# 13. 罗马数字转整数
class Solution:
    # def romanToInt(self, s: str) -> int:
    #     dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    #     dic_pre = {'M': 'C', 'D': 'C', 'C': 'X', 'L': 'X', 'X': 'I', 'V': 'I'}
    #     res = dic[s[-1]]
    #     for i in range(len(s)-2, -1, -1):
    #         if s[i+1] in dic_pre and s[i] == dic_pre[s[i+1]]:
    #             res -= dic[s[i]]
    #         else:
    #             res += dic[s[i]]
    #     return res

    # def romanToInt(self, s: str) -> int:
    #     dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    #     res = dic[s[-1]]
    #     for i, c in enumerate(s[:-1]):
    #         if dic[c] < dic[s[i+1]]:
    #             res -= dic[c]
    #         else:
    #             res += dic[c]
    #     return res

    # def romanToInt(self, s: str) -> int:
    #     dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     res = dic[s[-1]]
    #     for i in range(len(s)-2, -1, -1):
    #         if dic[s[i]] < dic[s[i+1]]:
    #             res -= dic[s[i]]
    #         else:
    #             res += dic[s[i]]
    #     return res

    # def romanToInt(self, s: str) -> int:
    #     dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #     res = dic[s[-1]]
    #     for i, c in enumerate(s[:-1]):
    #         if dic[c] < dic[s[i+1]]:
    #             res -= dic[c]
    #         else:
    #             res += dic[c]
    #     return res

    def romanToInt(self, s: str) -> int:
        dic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        res = dic[s[-1]]
        for i, c in enumerate(s[:-1]):
            if dic[c] < dic[s[i+1]]:
                res -= dic[c]
            else:
                res += dic[c]
        return res

s = Solution()
print(s.romanToInt("III"))

print(s.romanToInt("IV"))

print(s.romanToInt("IX"))

print(s.romanToInt("LVIII"))

print(s.romanToInt("MCMXCIV"))
