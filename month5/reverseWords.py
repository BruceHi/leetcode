# 翻转字符串
# 找更多的写法
import re
from collections import Iterable


class Solution:
#     def reverseWords(self, s: str) -> str:
#         p = r'[^ ]+'
#         pattern = re.compile(p)
#         res_list = pattern.findall(s)
#         return ' '.join(res_list[::-1])

    # def reverseWords(self, s: str) -> str:
    #     res = list(filter(lambda x: x != '', s.split(' ')))
    #     return ' '.join(res[::-1])

    # def reverseWords(self, s: str) -> str:
    #     return ' '.join(reversed(s.split()))  # 若是 split 里面不传参数，则是以任意空格字符串（一个或多个空格）分隔的。

    def reverseWords(self, s: str) -> str:
        print(s.split())
        return ' '.join(s.split()[::-1])


obj = Solution()
s = "the sky is blue"
print(obj.reverseWords(s))

s = "  hello world!  "
print(obj.reverseWords(s))

s = "a good   example"
print(obj.reverseWords(s))

s = "+---...2x+--x--+x-+-x2...---+"
print(obj.reverseWords(s))

s = "   one.   +two three?   ~four   !five- "
print(obj.reverseWords(s))
