# 字符串解码，数字可能不是 1 位的。
from collections import defaultdict
from collections import deque


class Solution:

    # DFS 失败！
    # def decodeString(self, s: str) -> str:
    #     res = []
    #
    #     n = len(s)
    #     def DFS(i):
    #         count = i
    #         for j in range(i+1, n):
    #
    #
    #     flag = 1
    #     for i in range(n):
    #         if '0' < s[i] <= '9' and flag == 1:
    #             DFS(i)
    #             flag += 1
    #         if s[i] == ']':
    #             flag -= 1

    # 维护一个栈，进栈时拼接字符串和数字。以失败告终。
    # 失败原因：字符串进栈有两个条件，一是碰到数字，二是碰到 ‘]’,而这时字符串又该出栈了。
    # 所以就失败了。
    # def decodeString(self, s: str) -> str:
    #     stack = []
    #     num, string = 0, ''
    #     for char in s:
    #         if char.isalpha():
    #             string += char
    #         elif char.isnumeric():
    #             num = num * 10 + int(char)
    #             stack.append(string)
    #             string = ''
    #         elif char == '[':
    #             stack.append(num)
    #             stack.append(char)
    #             num = 0
    #         else:
    #             stack.append(string)
    #             string = ''
    #
    #             tmp_s = stack.pop()
    #             stack.pop()  # 出去 ‘[’
    #             count = stack.pop()
    #             # tmp = string
    #             tmp = stack.pop() + tmp_s * count
    #             stack.append(tmp)
    #
    #     return ''.join(stack)

    # 维持一个栈，出栈时拼接成字符串
    # def decodeString(self, s: str) -> str:
    #     stack = []
    #     for char in s:
    #         tmp = ''
    #         if char != ']':
    #             stack.append(char)
    #         else:
    #             # 拼接字符，顺便把 [ 出栈了。
    #             c = stack.pop()
    #             while c != '[':
    #                 tmp = c + tmp
    #                 c = stack.pop()
    #             # 拼接数字
    #             count = ''
    #             while stack and stack[-1].isnumeric():  # 判空，是为了应对第一位为数字的情况 如 3[a 的情况
    #                 count = stack.pop() + count
    #
    #             stack.append(tmp * int(count))
    #     return ''.join(stack)

    # 入栈将字符串与前面数字绑定在一起
    def decodeString(self, s: str) -> str:
        stack, num, res = [], 0, ''
        for c in s:
            if c.isnumeric():
                num = num * 10 + int(c)  # 不能写成：num *= 10 + int(c)，会将后面视作整体与前面乘
            elif c == '[':
                stack.append([num, res])
                num, res = 0, ''
            elif c == ']':
                count, last_res = stack.pop()
                res = last_res + count * res
            else:
                res += c
        return res


obj = Solution()
s = "3[a2[c]]"
print(obj.decodeString(s))

s = "13[a]"
print(obj.decodeString(s))

s = "3[a]2[bc]"
print(obj.decodeString(s))


s = "2[abc]3[cd]ef"
print(obj.decodeString(s))

s = "100[leetcode]"
print(obj.decodeString(s))