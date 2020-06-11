# # 每日温度 再等待多久温度才会升高超过该日的天数
# # 暴力法会超时
# class Solution:
#     def dailyTemperatures(self, T):
#         day = []
#         for i in range(len(T)-1):
#             for j in range(i+1, len(T)):
#                 if T[i] < T[j]:
#                     day.append(j-i)
#                     break
#                 if j == len(T)-1:  # 注意临界值。
#                     day.append(0)
#         day.append(0)
#         return day
#
#
# # 本质上还是暴力
# # 让后面的数与前一位比较，若比他大得出结果为1，否则为0。再遍历一下单独计算为0的后面有无匹配的。
# # class Solution:
# #     def dailyTemperatures(self, T):
# #         day = []
# #         for i in range(len(T)-1):
# #             j = i + 1
# #             if T[j] > T[i]:
# #                 day.append(1)
# #             else:
# #                 day.append(0)
# #         day.append(0)
# #
# #         for i in range(len(day)-2):
# #             if day[i] == 0:
# #                 for j in range(i + 2, len(day)):
# #                     if T[i] < T[j]:
# #                         day[i] = j - i
# #                         break
# #         return day
#
# class Solution:
#     def dailyTemperatures(self, T):
#         stack = []  # 里面放的是T的索引
#         res = [0] * len(T)  # result
#         # res = [0 for _ in range(len(T))]
#         # for i in range(len(T)):
#         #     while stack and T[i] > T[stack[-1]]:  # 比栈内（索引小映射值）大的要处理
#         #         small = stack.pop()
#         #         res[small] = i - small
#         #     stack.append(i)  # 小的或栈为空，入栈。
#         for key, value in enumerate(T):
#             while stack and value > T[stack[-1]]:
#                 small = stack.pop()
#                 res[small] = key - small
#             stack.append(key)
#         return res

from typing import List


class Solution:
    # 递减栈，相同的也要入栈
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     stack, res = [], [0] * len(T)
    #     for i, t in enumerate(T):
    #         while stack and t > T[stack[-1][0]]:
    #             tmp = stack.pop()
    #             res[tmp[0]] = tmp[1]
    #         for s in stack:
    #             s[1] += 1
    #         stack.append([i, 1])
    #
    #     return res

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, res = [], [0] * len(T)
        for i, t in enumerate(T):
            while stack and t > T[stack[-1]]:
                tmp = stack.pop()
                res[tmp] = i - tmp
            stack.append(i)
        return res


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
s = Solution()
print(s.dailyTemperatures(temperatures))
