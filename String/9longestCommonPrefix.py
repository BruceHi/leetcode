# 最长公共前缀
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
def longestCommonPrefix(strs):
    prefix = ''
    for s in zip(*strs):
        if len(set(s)) == 1:
            prefix += s[0]
        else:
            break
    return prefix


list1 = ["aca","cba"]
print(longestCommonPrefix(list1))

list1 = ["flower","flow","flight"]
print(longestCommonPrefix(list1))

list1 = ["a","b"]
print(longestCommonPrefix(list1))

list1 = ["dog","racecar","car"]
print(longestCommonPrefix(list1))

list1 = []
print(longestCommonPrefix(list1))

