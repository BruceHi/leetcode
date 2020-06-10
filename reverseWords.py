# 翻转字符串
# 找更多的写法
import re


class Solution:
    def reverseWords(self, s: str) -> str:
        p = r'[^ ]+'
        pattern = re.compile(p)
        res_list = pattern.findall(s)
        return ' '.join(res_list[::-1])


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
