# 最长公共前缀
from typing import List


# def longestCommonPrefix(strs):
#     if len(strs) == 0:
#         return ''
#     res = strs[0]
#     count = 0
#
#     for i in range(1, len(strs)):
#         for j in range(min(len(res), len(strs[i]))):
#             if res[:j+1] == strs[i][:j+1]:
#                 count += 1
#         res = res[:count]
#         count = 0
#         if res == '':
#             return ''
#     return res

    # # 使用切片
    #     # i = 1
    #     # while i < len(strs):
    #     #     for j in range(min(len(res), len(strs[i]))):
    #     #         if res[j] == strs[i][j]:
    #     #             count += 1
    #     #     res = res[:count]
    #     #     count = 0  # 莫忘了重置
    #     #     if res == '':
    #     #         return ''
    #     #     i += 1
    #     # return res


# def longestCommonPrefix(strs):
#     if not len(strs):
#         return ''
#     prefix = strs[0]
#     for s in strs[1:]:
#         while not s.startswith(prefix):  # 当找到前缀了，退出循环，找下一个。同时更新前缀。
#             prefix = prefix[:len(prefix) - 1]
#             if not prefix:
#                 return ''
#
#     return prefix


# 使用解包，打包，集合
# def longestCommonPrefix(strs):
#     prefix = ''
#     for s in zip(*strs):
#         if len(set(s)) == 1:
#             prefix += s[0]
#         else:
#             break
#     return prefix


# # min 和 max 对字符串排序是按字典序排序
# def longestCommonPrefix(strs):
#     if not strs:
#         return ''
#     s1, s2 = min(strs), max(strs)
#     for i, c in enumerate(s1):
#         if c != s2[i]:
#             return s1[:i]
#     return s1

# # 构建字典树
# def longestCommonPrefix(strs):
#     if not strs:
#         return ''
#
#     root = {}
#     for word in strs:
#         if not word:
#             return ''
#         node = root
#         for char in word:
#             node = node.setdefault(char, {})
#         node['#'] = '#'
#
#     res, node = '', root
#     while node != {'#': '#'}:
#         if len(node) == 1:
#             char = str(*node)
#             res += char
#             node = node[char]
#         else:
#             return res
#     return res


# def longestCommonPrefix(strs):
#     if not strs:
#         return ''
#
#     prefix = strs[0]
#     for s in strs[1:]:
#         while not s.startswith(prefix):
#             prefix = prefix[:len(prefix)-1]
#             if not prefix:
#                 return ''
#     return prefix


# def longestCommonPrefix(strs: List[str]) -> str:
#     if not strs:
#         return ''
#     s1, s2 = min(strs), max(strs)
#     for i, c in enumerate(s1):
#         if c != s2[i]:
#             return s1[:i]
#     return s1

def longestCommonPrefix(strs):
    if not strs:
        return ''
    root = {}
    for word in strs:
        if not word:
            return ''
        node = root
        for c in word:
            node = node.setdefault(c, {})
        node['#'] = '#'

    res, node = '', root
    while node != {'#': '#'}:
        if len(node) == 1:
            c, = node
            res += c
            node = node[c]
        else:
            break
    return res


list1 = ["abc","abc"]
print(longestCommonPrefix(list1))

list1 = ["","b"]
print(longestCommonPrefix(list1))

list1 = ["aca","cba"]
print(longestCommonPrefix(list1))

list1 = ["flower","flow","flight"]
print(longestCommonPrefix(list1))

list1 = ["a","b"]
print(longestCommonPrefix(list1))

list1 = ["dog","racecar","caraaaaa"]
print(longestCommonPrefix(list1))

list1 = []
print(longestCommonPrefix(list1))

list1 = ['a', 'ab']
print(longestCommonPrefix(list1))

list1 = ['']
print(longestCommonPrefix(list1))
