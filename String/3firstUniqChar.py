# 字符串中的第一个唯一字符

# from collections import Counter
#
#
# def firstUniqChar(s: str) -> int:
#     count = Counter(s)
#
#     for i, c in enumerate(s):
#         if count[c] == 1:
#             return i
#
#     return -1

from collections import OrderedDict

# def firstUniqChar(s: str) -> int:
#     hash_map = OrderedDict()
#     for i, c in enumerate(s):
#         if c in hash_map:
#             hash_map[c] = -1
#         else:
#             hash_map[c] = i
#
#     for i in hash_map.values():
#         if i != -1:
#             return i
#
#     return -1


# def firstUniqChar(s) -> int:
#     dic = {}
#     for i, char in enumerate(s):
#         if char not in dic:
#             dic[char] = i
#         else:
#             dic[char] = -1
#
#     for i, char in enumerate(s):
#         if dic[char] != -1:
#             return i
#
#     return -1

from collections import Counter


# def firstUniqChar(s: str) -> int:
#     dic = Counter(s)
#     for i, c in enumerate(s):
#         if dic[c] == 1:
#             return i
#     return -1

class Solution:
    # def firstUniqChar(self, s: str) -> int:
    #     for i, c in enumerate(s):
    #         if c not in set(s[:i] + s[i+1:]):
    #             return i
    #     return -1

    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1


obj = Solution()
s = "aadadaad"  # 最后一个重复
print(obj.firstUniqChar(s))

s = ""
print(obj.firstUniqChar(s))

s = "loveleetcode"
print(obj.firstUniqChar(s))

s = "leetcode"
print(obj.firstUniqChar(s))

s = "eeec"
print(obj.firstUniqChar(s))

s = 'eaabb'
print(obj.firstUniqChar(s))
