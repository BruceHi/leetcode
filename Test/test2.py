# # n = input()
#
#
# # def more(self, s):
# #     for i in range(len(s)):
# #         new = s[i:] + s[:i]
# #         return new
#
# # s = 'abc'
# # for i in range(len(s)):
# #     new = s[i:] + s[:i]
# #     print(new)
#
#
# # def function(s):
# #     for i in range(len(s)):
# #         new = s[i:] + s[:i]
# #         if isPalindrome(new):
# #             return True
# #     return False
# #
# #
# # def isPalindrome(s):
# #     left, right = 0, len(s) - 1
# #     while left < right:
# #         if s[left] != s[right]:
# #             return False
# #         left, right = left + 1, right - 1
# #     return True
#
#
# def function(num):
#     if int(''.join(sorted(str(num), reverse=True))) > num:
#         return False
#     tmp = sorted(str(num), reverse=True)
#     tmp[-1], tmp[-2] = tmp[-2], tmp[-1]
#     return int(''.join(tmp))
#
#
#
# # print(function('abcba'))
# #
# # print(function('bcbaa'))
#
# print(function(12345))
# print(function(1100))
#
# print(ord('a'))
# print(chr(98))
#
# print('80' < '25')
#
# a = {1, 2, 3}
# b = map(lambda x: x+1, a)
#
# print(list(b))

from collections import OrderedDict

# def firstHeight(n, nums):
#     res = [-1]
#     flag = 1
#     for i in range(1, n):
#         for j in range(i-1, -1, -1):
#             if nums[j] > nums[i]:
#                 res.append(nums[j])
#                 flag = 0
#                 break
#         if flag:
#             res.append(-1)
#     return res


def firstHeight(n, nums):
    res, dic = [], OrderedDict()
    for i, num in enumerate(nums):
        tmp = list(filter(lambda x: x > nums[i], dic))
        dic[num] = i
        if tmp:
            res.append(tmp[-1])
        else:
            res.append(-1)
    return res


n = 5
nums = [5, 4, 3, 2, 1]
print(firstHeight(n, nums))

n = 5
nums = [1, 2, 3, 4, 5]
print(firstHeight(n, nums))

from collections import defaultdict


def minWindow(s: str, t: str) -> str:
    need = defaultdict(int)
    for c in t:
        need[c]+=1
    needCnt=len(t)
    i=0
    res=(0,float('inf'))
    for j,c in enumerate(s):
        if need[c]>0:
            needCnt-=1
        need[c]-=1
        if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
            while True:      #步骤二：增加i，排除多余元素
                c=s[i]
                if need[c]==0:
                    break
                need[c]+=1
                i+=1
            if j-i<res[1]-res[0]:   #记录结果-
                res=(i,j)
            need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
            needCnt+=1
            i+=1
    return t if res[1]>len(s) else s[res[0]:res[1]+1]    #如果res始终没被更新过，代表无满足条件的结果


# s = 'ADKSBACWDMVJDNAHFNFJ'
# t = 'ABCD'
# print(minWindow(s, t))
#
# s = 'ABCD'
# t = 'ABCD'
# print(minWindow(s, t))

# s = 'ADKSBACWDMVJDNAHFNFJ'
# t = 'ABCD'

s, t = input().split()
need = defaultdict(int)
for c in t:
    need[c]+=1
needCnt=len(t)
i=0
res=(0,float('inf'))
for j,c in enumerate(s):
    if need[c]>0:
        needCnt-=1
    need[c]-=1
    if needCnt==0:       #步骤一：滑动窗口包含了所有T元素
        while True:      #步骤二：增加i，排除多余元素
            c=s[i]
            if need[c]==0:
                break
            need[c]+=1
            i+=1
        if j-i<res[1]-res[0]:   #记录结果
            res=(i,j)
        need[s[i]]+=1  #步骤三：i增加一个位置，寻找新的满足条件滑动窗口
        needCnt+=1
        i+=1
print(t) if res[1]>len(s) else print(s[res[0]:res[1]+1])
