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


def firstUniqChar(s: str) -> int:
    dic = Counter(s)
    for i, c in enumerate(s):
        if dic[c] == 1:
            return i
    return -1


s = "aadadaad"  # 最后一个重复
print(firstUniqChar(s))

s = ""
print(firstUniqChar(s))

s = "loveleetcode"
print(firstUniqChar(s))

s = "leetcode"
print(firstUniqChar(s))

s = "eeec"
print(firstUniqChar(s))

s = 'eaabb'
print(firstUniqChar(s))
