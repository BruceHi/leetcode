# 43. 字符串相乘
class Solution:
    # def multiply(self, num1: str, num2: str) -> str:
    #     return str(int(num1) * int(num2))

    def multiply(self, num1: str, num2: str) -> str:
        return str(eval(num1 + '*' + num2))


s = Solution()
num1 = "2"
num2 = "3"
print(s.multiply(num1, num2))

num1 = "123"
num2 = "456"
print(s.multiply(num1, num2))