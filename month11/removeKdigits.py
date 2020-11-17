# 移掉 k 位数字
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while k and stack and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)

        # tmp = stack[:-k] if k else stack
        # res = ''.join(tmp).lstrip('0')  # 第二种
        # return res if res else '0'  # 和第三种情况

        res = stack[:-k] if k else stack
        return ''.join(res).lstrip('0') or '0'


s = Solution()
num = "1432219"
k = 3
print(s.removeKdigits(num, k))

num = "10200"
k = 1
print(s.removeKdigits(num, k))

num = "10"
k = 2
print(s.removeKdigits(num, k))

num = "10"
k = 1
print(s.removeKdigits(num, k))