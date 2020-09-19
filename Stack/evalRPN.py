# 逆波兰式
import operator
from typing import List


class Solution:
    # def evalRPN(self, tokens):
    #     # 符号-操作（函数）字典
    #     ops = {'+': operator.add, '-': operator.sub,
    #            '*': operator.mul, '/': operator.truediv}
    #     num = []
    #     for i in tokens:
    #         # if i.isdigit():  # i是字符串类型才能判断。没法判断'-11'不是数字
    #         if i not in ops:
    #             num.append(int(i))
    #         else:
    #             b, a = num.pop(), num.pop()
    #             new = int(ops[i](a, b))  # 特别处理'/'：要求除法保留小数位
    #             num.append(new)
    #     return num.pop()

    # def evalRPN(self, tokens: List[str]) -> int:
    #     stack = []
    #     op = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': lambda x, y: int(x / y)}
    #     for c in tokens:
    #         if c not in op:
    #             stack.append(int(c))
    #         else:
    #             a, b = stack.pop(), stack.pop()
    #             stack.append(op[c](b, a))
    #     return stack.pop()

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c not in '+-*/':
                stack.append(c)
            else:
                a, b = stack.pop(), stack.pop()
                stack.append(str(int(eval(b + c + a))))
        return int(stack.pop())


s = Solution()
c = ["2", "1", "+", "3", "*"]
print(s.evalRPN(c))

c = ["4", "13", "5", "/", "+"]
print(s.evalRPN(c))

c = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(s.evalRPN(c))