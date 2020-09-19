# # bf算法，可以使用切片。暴力法
# def strStr(haystack, needle):
#     for i in range(len(haystack) - len(needle) + 1):
#         if haystack[i: i+len(needle)] == needle:
#             return i
#
#     return -1


# # KMP算法初步实现
# def strStr(s, p):
#     if len(p) == 0:
#         return 0
#
#     if len(s) < len(p):
#         return -1
#
#     def getNext(x):  # 求的其实是大多数人所说的pmt,别人的next是整体要右移一下。
#         for i in range(x, 0, -1):  # 使用倒叙，是因为统计的next数组都是需要最长的。
#             if p[0:i] == p[x - i + 1:x + 1]:
#                 return i
#         return 0
#
#     nxt = [getNext(x) for x in range(len(p))]
#
#     tar = 0  # 主串
#     pos = 0  # 模式串
#
#     while tar < len(s):
#         if s[tar] == p[pos]:
#             tar += 1
#             pos += 1
#         elif pos:
#             pos = nxt[pos-1]
#         else:
#             tar += 1
#
#         if pos == len(p):
#             return tar - pos
#
#     return -1


# KMP算法改进next的获取
# def strStr(haystack, needle):
#     # if len(needle) == 0:
#     #     return 0
#     #
#     # if len(haystack) < len(needle):
#     #     return -1
#
#
#     def buildnext(nxt):
#         nxt.append(0)
#         x = 1  # nxt索引
#         now = 0
#
#         while x < len(needle):
#             if needle[now] == needle[x]:
#                 now += 1
#                 x += 1
#                 nxt.append(now)
#             elif now:
#                 now = nxt[now-1]  # 一旦缩小，会进行下次遍历，直至找到值。
#             else:
#                 nxt.append(0)
#                 x += 1
#
#     nxt = []
#     buildnext(nxt)
#
#     tar = 0  # 主串
#     pos = 0  # 模式串
#
#     while tar < len(haystack):
#         if haystack[tar] == needle[pos]:
#             tar += 1
#             pos += 1
#         elif pos:
#             pos = nxt[pos-1]
#         else:
#             tar += 1
#
#         if pos == len(needle):
#             return tar - pos
#
#     return -1

# bf算法，可以使用切片。暴力法
# def strStr(haystack, needle):
#     return haystack.find(needle)


# Sunday 算法
# def strStr(haystack, needle):
#     if not needle or not haystack:
#         return 0
#     if len(needle) > len(haystack):
#         return -1
#
#     # 原始串索引(记录匹配到的最后一个索引的下一个索引)，匹配串索引
#     hay_idx, needle_idx = 0, 0
#     while needle_idx < len(needle):
#         if hay_idx > len(haystack) - 1:
#
#     return hay_idx - needle_idx  # 退出 while 循环时，needle_index

# def strStr(haystack, needle):
#     return haystack.find(needle)

def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)


haystack = "mississippi"
needle = "issip"
print(strStr(haystack, needle))

haystack = "aaa"
needle = "aaaa"
print(strStr(haystack, needle))

haystack = "hello"
needle = ""
print(strStr(haystack, needle))

haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))

haystack = "aaaaa"
needle = "bba"
print(strStr(haystack, needle))

