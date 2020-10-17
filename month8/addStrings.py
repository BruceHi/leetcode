# 与 2 题相似
class Solution:
    # def addStrings(self, num1: str, num2: str) -> str:
    #     return str(int(num1) + int(num2))

    # def addStrings(self, num1: str, num2: str) -> str:
    #     i, j = len(num1)-1, len(num2)-1
    #     carry = 0
    #     res = ''
    #     while i >= 0 or j >= 0 or carry:
    #         x = ord(num1[i]) - ord('0') if i >= 0 else 0
    #         y = ord(num2[j]) - ord('0') if j >= 0 else 0
    #         tmp = x + y + carry
    #         carry, val = divmod(tmp, 10)
    #         res = str(val) + res
    #         i, j = i - 1, j - 1
    #     return res

    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        s = 0
        res = ''
        while i >= 0 or j >= 0 or s:
            x = ord(num1[i]) - ord('0') if i >= 0 else 0
            y = ord(num2[j]) - ord('0') if j >= 0 else 0
            s += x + y
            res = str(s % 10) + res
            s //= 10
            i, j = i-1, j-1
        return res

    # def addStrings(self, num1: str, num2: str) -> str:
    #     return str(eval(num1 + '+' + num2))


s = Solution()
print(s.addStrings('119', '29'))
