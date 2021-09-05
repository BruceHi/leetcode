# 227. 基本计算器 2
from operator import add, truediv, sub, mul


class Solution:
    # 双栈
    # def calculate(self, s: str) -> int:
    #     stack1, stack2 = [], []
    #     n = len(range)
    #     for i, c in enumerate(s):
    #         if not c:
    #             continue
    #         if c.isdigit():
    #             if not stack1:
    #                 stack1.append(int(c))
    #             if s[i-1].isdigit():
    #                 stack1.append(stack1.pop() * 10 + int(c))
    #         elif

    # def calculate(self, s: str) -> int:
    #     stack = []
    #     i = 0
    #     n = len(s)
    #     num = 0
    #     op = '+'
    #     while i < n:
    #         if s[i] == ' ':
    #             i += 1
    #             continue
    #         if s[i] in ['+', '-', '*', '/']:
    #             op = s[i]
    #             i += 1
    #             continue
    #         while i < n and s[i].isdigit():
    #             num = num * 10 + int(s[i])
    #             i += 1
    #         if op == '*':
    #             stack.append(stack.pop() * num)
    #         elif op == '/':
    #             stack.append(int(stack.pop() / num))
    #         elif op == '-':
    #             stack.append(-num)
    #         else:
    #             stack.append(num)
    #         num = 0
    #     return sum(stack)

    # pre_op 代表的是先前的运算符
    # def calculate(self, s: str) -> int:
    #     stack = []
    #     pre_op = '+'
    #     num = 0
    #     for i, c in enumerate(s):
    #         if c.isdigit():
    #             num = num * 10 + int(c)
    #         if i == len(s)-1 or c in '+-*/':
    #             if pre_op == '*':
    #                 stack.append(stack.pop() * num)
    #             elif pre_op == '/':
    #                 stack.append(int(stack.pop() / num))
    #             elif pre_op == '-':
    #                 stack.append(-num)
    #             else:
    #                 stack.append(num)
    #             pre_op = c
    #             num = 0
    #     return sum(stack)

    # def calculate(self, s: str) -> int:
    #     return eval(s.replace('/', '//'))

    # def calculate(self, s: str) -> int:
    #     stack = []
    #     pre_op = "+"
    #     num = 0
    #     for i, c in enumerate(s):
    #         if c.isdigit():
    #             num = num * 10 + int(c)
    #         # if i == len(s) - 1 or not c.isdigit():  # 错误
    #         if i == len(s) - 1 or c in '+-*/':  # 排除空格的影响
    #             if pre_op == '*':
    #                 # stack.append(stack.pop() * num)
    #                 stack[-1] *= num
    #             elif pre_op == '/':
    #                 stack.append(int(stack.pop() / num))
    #             elif pre_op == '-':
    #                 stack.append(-num)
    #             else:
    #                 stack.append(num)
    #             pre_op = c
    #             num = 0
    #     return sum(stack)

    def calculate(self, s: str) -> int:
        stack = []
        pre_op = "+"
        num = 0
        for i, c in enumerate(s):
            if c.isdigit():
                num = num * 10 + int(c)
            # if i == len(s) - 1 or not c.isdigit():  # 错误
            if i == len(s) - 1 or c in '+-*/':  # 排除空格的影响
                if pre_op == '*':
                    # stack.append(stack.pop() * num)
                    stack[-1] *= num
                elif pre_op == '/':
                    stack.append(int(stack.pop() / num))
                elif pre_op == '-':
                    stack.append(-num)
                else:
                    stack.append(num)
                pre_op = c
                num = 0
        return sum(stack)

    # def calculate(self, s: str) -> int:
    #     stack = []
    #     s += '$'
    #     pre_flag = '+'
    #     num = 0
    #
    #     for c in s:
    #         if c.isdigit():
    #             num = num * 10 + int(c)
    #         elif c == ' ':
    #             continue
    #         else:
    #             if pre_flag == '+':
    #                 stack.append(num)
    #             elif pre_flag == '-':
    #                 stack.append(-num)
    #             elif pre_flag == '*':
    #                 stack.append(stack.pop() * num)
    #             elif pre_flag == '/':
    #                 stack.append(int(stack.pop() / num))
    #             pre_flag = c
    #             num = 0
    #     return sum(stack)


obj = Solution()
s = "3+2*2"
print(obj.calculate(s))

s = " 3/2 "
print(obj.calculate(s))

s = " 3+5 / 2 "
print(obj.calculate(s))

s = " 3/2+ 3/2"
print(obj.calculate(s))

s = "14/3*2"
print(obj.calculate(s))
