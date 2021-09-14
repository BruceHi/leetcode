# 678. 有效的括号字符串
class Solution:
    # def checkValidString(self, s: str) -> bool:
    #     left, star = [], []
    #     for i, c in enumerate(s):
    #         if c == '(':
    #             left.append(i)
    #         elif c == '*':
    #             star.append(i)
    #         else:
    #             if left:
    #                 left.pop()
    #             elif star:
    #                 star.pop()
    #             else:
    #                 return False
    #     while left and star:
    #         if left[-1] > star[-1]:
    #             return False
    #         left.pop()
    #         star.pop()
    #     return not left

    def checkValidString(self, s: str) -> bool:
        left, star = [], []
        for i, c in enumerate(s):
            if c == '(':
                left.append(i)
            elif c == '*':
                star.append(i)
            else:
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while left and star:
            if left[-1] > star[-1]:
                return False
            left.pop()
            star.pop()
        return not left


obj = Solution()
s = "()"
print(obj.checkValidString(s))

s = "(*)"
print(obj.checkValidString(s))

s = "(*))"
print(obj.checkValidString(s))
