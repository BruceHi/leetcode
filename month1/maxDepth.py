# 1614. 括号的最大嵌套深度
class Solution:
    def maxDepth(self, s: str) -> int:
        # size 为 栈的大小
        res, size = 0, 0
        for c in s:
            if c == '(':
                size += 1
                res = max(res, size)
            elif c == ')':
                size -= 1
        return res


obj = Solution()
s = "(1+(2*3)+((8)/4))+1"
print(obj.maxDepth(s))

s = "(1)+((2))+(((3)))"
print(obj.maxDepth(s))

s = "1+(2*3)/(2-1)"
print(obj.maxDepth(s))

s = "1"
print(obj.maxDepth(s))
