# 640.求解方程
class Solution:
    # def solveEquation(self, equation: str) -> str:
    #     num, coe = 0, 0
    #     tmp = 0
    #     sign = 1
    #     flag = 1
    #     for i, e in enumerate(equation + '+'):
    #         if e == '=':
    #             if equation[i-1] != 'x':
    #                 num += flag * sign * tmp
    #                 tmp = 0
    #             flag = -1
    #             sign = 1
    #         elif e.isnumeric():
    #             tmp = tmp * 10 + int(e)
    #         elif e == 'x':
    #             if i == 0 or equation[i-1] in '+-=':
    #                 tmp = 1
    #             coe += flag * sign * tmp
    #             tmp = 0
    #         else:
    #             if i != 0 and equation[i-1] != 'x':
    #                 num += flag * sign * tmp
    #                 tmp = 0
    #             if e == '-':
    #                 sign = -1
    #             else:
    #                 sign = 1
    #     if coe == 0:
    #         if num == 0:
    #             return "Infinite solutions"
    #         else:
    #             return "No solution"
    #     else:
    #         return 'x=' + str(-num // coe)


    # def solveEquation(self, equation: str) -> str:
    #     num, coe = 0, 0
    #     tmp = 0
    #     sign = 1
    #     flag = 1
    #     for i, e in enumerate(equation + '+'):
    #         if e.isnumeric():
    #             tmp = tmp * 10 + int(e)
    #         elif e == 'x':
    #             if i == 0 or equation[i-1] in '+-=':
    #                 tmp = 1
    #             coe += flag * sign * tmp
    #             tmp = 0
    #         else:  # -+=
    #             if i != 0 and equation[i-1] != 'x':
    #                 num += flag * sign * tmp
    #                 tmp = 0
    #             if e == '-':
    #                 sign = -1
    #             else:  # +=
    #                 sign = 1
    #             if e == '=':
    #                 flag = -1
    #
    #     if coe == 0:
    #         if num == 0:
    #             return "Infinite solutions"
    #         else:
    #             return "No solution"
    #     return 'x=' + str(-num // coe)

    # def solveEquation(self, equation: str) -> str:
    #     num, coe = 0, 0
    #     flag, sign = 1, 1
    #     tmp = 0
    #     for i, e in enumerate(equation + '+'):
    #         if e.isnumeric():
    #             tmp = tmp * 10 + int(e)
    #         elif e == 'x':
    #             if i == 0 or equation[i-1] in '+-=':
    #                 tmp = 1
    #             coe += flag * sign * tmp
    #             tmp = 0
    #         else:
    #             if i != 0 and equation[i-1].isnumeric():
    #                 num += flag * sign * tmp
    #                 tmp = 0
    #             if e == '-':
    #                 sign = -1
    #             else:
    #                 sign = 1
    #             if e == '=':
    #                 flag = -1
    #
    #     if coe == 0:
    #         if num == 0:
    #             return 'Infinite solutions'
    #         else:
    #             return 'No solution'
    #
    #     return 'x=' + str(-(num // coe))


    def solveEquation(self, equation: str) -> str:
        coe, num = 0, 0
        flag, sign = 1, 1
        tmp = 0
        for i, e in enumerate(equation + '+'):
            if e.isnumeric():
                tmp = tmp * 10 + int(e)
            elif e == 'x':
                if i == 0 or equation[i-1] in '+-=':
                    tmp = 1
                coe += flag * sign * tmp
                tmp = 0
            else:
                if i != 0 and equation[i-1].isnumeric():
                    num += flag * sign * tmp
                    tmp = 0
                if e == '=':
                    flag = -1
                if e == '-':
                    sign = -1
                else:
                    sign = 1

        if coe == 0:
            if num != 0:
                return "No solution"
            return 'Infinite solutions'
        return 'x=' + str(-num // coe)


s = Solution()
equation = "x+5-3+x=6+x-2"
print(s.solveEquation(equation))

equation = "x=x"
print(s.solveEquation(equation))

equation = "2x=x"
print(s.solveEquation(equation))

# print(eval('+5+-3+-6+--2'))

equation = "2x+3x-6x=x+2"
print(s.solveEquation(equation))

equation = "x=x+2"
print(s.solveEquation(equation))

equation = "0x=0"
print(s.solveEquation(equation))
