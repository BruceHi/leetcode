# 1006.笨阶乘
from itertools import cycle
from operator import add, sub, mul, floordiv

# 地板除，都是正数正确，有负数就错误了

class Solution:

    # 使用数字栈和符号栈
    # def clumsy(self, N: int) -> int:
    #     op_gen = cycle(['*', '//', '+', '-'])
    #     dic = {'*': mul, '//': floordiv, '+': add, '-': sub}
    #     stack, op = [], []
    #     for i in range(N, 0, -1):
    #         if op and op[-1] in ['*', '//']:
    #             num1 = stack.pop()
    #             stack.append(dic[op.pop()](num1, i))
    #         else:
    #             stack.append(i)
    #         op.append(next(op_gen))
    #     res = stack[0]
    #     for i, c in enumerate(op[:-1]):
    #         res = dic[c](res, stack[i+1])
    #     return res

    # 使用一个栈，使用循环控制乘除加减
    def clumsy(self, N: int) -> int:
        op = 0
        stack = [N]
        for i in range(N-1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                stack.append(int(stack.pop() / i))
            elif op == 2:
                stack.append(i)
            else:
                stack.append(-i)
            op = (op + 1) % 4
        return sum(stack)


s = Solution()
n = 4
print(s.clumsy(n))

n = 10
print(s.clumsy(n))
