# 反序双层循环，便


# hash_map
# def firstUniqChar(s):
#     hash_map = {}
#     for i in range(len(s)):
#         if hash_map.get(s[i]) is not None:
#             hash_map[s[i]] = -1
#             continue
#         hash_map[s[i]] = i
#
#     # for i in hash_map.values():
#     #     if i != -1:
#     #         return i
#
#     return hash_map


from collections import Counter


# # hash_map
# def firstUniqChar(s):
#
#     count = Counter(s)
#     for idx, ch in enumerate(s):
#         if count[ch] == 1:
#             return idx
#
#     return -1


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


def firstUniqChar(s: str) -> int:
    hash_map = OrderedDict()
    for i, c in enumerate(s):
        if c in hash_map:
            hash_map[c] = -1
        else:
            hash_map[c] = i

    for i in hash_map.values():
        if i != -1:
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
