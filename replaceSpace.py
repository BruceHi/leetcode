# 剑指 offer 05.替换空格
class Solution:
    def replaceSpace(self, s: str) -> str:
        return s.replace(' ', '%20')

obj = Solution()
s = "We are happy."
print(obj.replaceSpace(s))
