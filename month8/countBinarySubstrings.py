# 计数二进制字串
from functools import reduce
from collections import defaultdict


class Solution:

    # # 正确，但超时
    # def countBinarySubstrings(self, s: str) -> int:
    #     res = 0
    #     n = len(s)
    #     for i in range(n-1):
    #         count = 1
    #         for j in range(i+1, n):
    #             if s[j] == s[i]:
    #                 count += 1
    #             else:
    #                 if s[j: j + count] == s[j] * count:
    #                     res += 1
    #                 break
    #     return res

    # 超时
    # def countBinarySubstrings(self, s: str) -> int:
    #     res = 0
    #     n = len(s)
    #     i = 0
    #     while i < n-1:
    #         count = 1
    #         for j in range(i+1, n):
    #             if s[j] == s[i]:
    #                 count += 1
    #                 if j == n-1:
    #                     return res
    #             else:
    #                 if s[j: j + count] == s[j] * count:
    #                     res += count
    #                     i += count
    #                 else:
    #                     i += 1
    #                 break
    #     return res

    # 写得不好
    # def countBinarySubstrings(self, s: str) -> int:
    #     nums = [float('inf')]
    #     res = 0
    #     i = 0
    #     for j in range(1, len(s)):
    #         if s[i] != s[j]:
    #             res += min(nums[-1], j-i)
    #             nums.append(j-i)
    #             i = j
    #     res += min(nums[-1], len(s) - i)
    #     nums.append(len(s) - i)
    #     return res - nums[1]

    # def countBinarySubstrings(self, s: str) -> int:
    #     nums = []
    #     i = 0
    #     for j in range(1, len(s)):
    #         if s[i] != s[j]:
    #             nums.append(j-i)
    #             i = j
    #     nums.append(len(s) - i)
    #     res = 0
    #     for i in range(1, len(nums)):
    #         res += min(nums[i-1], nums[i])
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     count = 0
    #     res = 0
    #     i = 0
    #     for j in range(1, len(s)):
    #         if s[i] != s[j]:
    #             res += min(count, j-i)
    #             count = j - i
    #             i = j
    #     res += min(count, len(s)-i)
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     count = 0
    #     res = 0
    #     i = 0
    #     for j, c in enumerate(s):
    #         if c != s[i]:
    #             res += min(count, j-i)
    #             count = j - i
    #             i = j
    #     res += min(count, len(s)-i)
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     nums = []
    #     i = 0
    #     for j, c in enumerate(s):
    #         if c != s[i]:
    #             nums.append(j-i)
    #             i = j
    #     nums.append(len(s) - i)
    #     res = 0
    #     for i in range(1, len(nums)):
    #         res += min(nums[i-1], nums[i])
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     count = 0
    #     res = 0
    #     i = 0
    #     for j, c in enumerate(s):
    #         if c != s[i]:
    #             res += min(count, j - i)
    #             count = j - i
    #             i = j
    #     res += min(count, len(s)-i)
    #     return res

    # 理解错误
    # def countBinarySubstrings(self, s: str) -> int:
    #     res = 0
    #     dic = defaultdict(int)
    #     dic[0] = 1
    #     prefix = 0
    #     for c in s:
    #         if c == '0':
    #             prefix -= 1
    #         else:
    #             prefix += 1
    #         res += dic[prefix]
    #         dic[prefix] += 1
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     nums = []
    #     i = 0
    #     for j, c in enumerate(s):
    #         if s[i] != c:
    #             nums.append(j-i)
    #             i = j
    #     nums.append(len(s)-i)
    #
    #     res = 0
    #     for i, num in enumerate(nums[:-1]):
    #         res += min(num, nums[i+1])
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     res = 0
    #     count = 0
    #     i = 0
    #     for j, c in enumerate(s):
    #         if s[i] != c:
    #             res += min(count, j-i)
    #             count = j-i
    #             i = j
    #     res += min(count, len(s)-i)
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     res, i = 0, 0
    #     cur = 0
    #     for j, c in enumerate(s):
    #         if s[i] != c:
    #             res += min(cur, j - i)
    #             cur = j - i
    #             i = j
    #     res += min(cur, len(s)-i)
    #     return res

    # def countBinarySubstrings(self, s: str) -> int:
    #     i, count = 0, 0
    #     res = 0
    #     for j, c in enumerate(s):
    #         if c != s[i]:
    #             res += min(count, j-i)
    #             count = j - i
    #             i = j
    #     return res + min(count, len(s)-i)

    # def countBinarySubstrings(self, s: str) -> int:
    #     i = res = 0
    #     count = 0
    #     for j, c in enumerate(s):
    #         if c != s[i]:
    #             res += min(count, j - i)
    #             count = j - i
    #             i = j
    #     res += min(count, len(s) - i)
    #     return res

    def countBinarySubstrings(self, s: str) -> int:
        res = i = 0
        count = 0
        for j, c in enumerate(s):
            if c != s[i]:
                res += min(count, j-i)
                count = j - i
                i = j
        return res + min(count, len(s)-i)



obj = Solution()
print(obj.countBinarySubstrings("00110011"))

print(obj.countBinarySubstrings("10101"))

print(obj.countBinarySubstrings("1"))

print(obj.countBinarySubstrings("101"))
