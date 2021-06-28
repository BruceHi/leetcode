# 剑指 offer20. 表示数值的字符串
# 65. 有效数字
import re


class Solution:
    # def isNumber(self, s: str) -> bool:
    #     s = s.strip()
    #     # 整数、带 e（e 后面可以带+-号） 的整数数、小数（除了 .123 之类的）、.1 之类的 .在最开始的小数（+.8 也算对的）
    #     # 带 e 的小数情况1，带e 的小数情况2
    #     p = r'^[-+]?\d+$|^[-+]?\d+[eE][-+]?\d+$|^[-+]?\d+\.\d*$|' \
    #         r'^[-+]?\.\d+$|^[-+]?\d+\.\d*[eE][-+]?\d+$|^[-+]?\.\d+[eE][-+]?\d+$'
    #     pattern = re.compile(p)
    #     if pattern.match(s):
    #         return True
    #     else:
    #         return False

    # 测试地址：https://regex101.com/r/LknU0u/2/
    # def isNumber(self, s: str) -> bool:
    #     p = r'^[-+]?((\d+)|(\d+\.\d*)|(\.\d+))([eE][-+]?\d+)?$'
    #     pattern = re.compile(p)
    #     return pattern.match(s.strip()) is not None

    # def isNumber(self, s: str) -> bool:
    #     try:
    #         float(s)
    #     except:
    #         return False
    #     return True

    def isNumber(self, s: str) -> bool:
        p = r'^[+-]?((\d+)|(\.\d+)|(\d+\.\d*))([eE][+-]?\d+)?$'
        pattern = re.compile(p)
        return pattern.match(s.strip()) is not None


obj = Solution()
s = "0"
print(obj.isNumber(s))

s = "e"
print(obj.isNumber(s))

s = "."
print(obj.isNumber(s))

s = "    .1  "
print(obj.isNumber(s))

s = "3."
print(obj.isNumber(s))

s = "+.8"
print(obj.isNumber(s))

s = "46.e3"
print(obj.isNumber(s))

s = ".2e81"
print(obj.isNumber(s))

s = " 005047e+6"
print(obj.isNumber(s))
