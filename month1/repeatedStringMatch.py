# 686. 重复叠加字符串匹配
class Solution:
    # 关键在于终止长度，2*A+B
    # def repeatedStringMatch(self, a: str, b: str) -> int:
    #     if set(b) - set(a):
    #         return -1
    #     n = len(a + b + a)
    #     i = 1
    #     while i <= n:
    #         if b in a * i:
    #             return i
    #         i += 1
    #     return -1

    # 其实a 扩充后的长度 <= a + b 也说得通。
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if set(b) - set(a):
            return -1
        n = len(a + b)
        i = 1
        while i <= n:
            if b in a * i:
                return i
            i += 1
        return -1



s = Solution()
a = "abcd"
b = "cdabcdab"
print(s.repeatedStringMatch(a, b))

a = "a"
b = "aa"
print(s.repeatedStringMatch(a, b))

a = "a"
b = "a"
print(s.repeatedStringMatch(a, b))

a = "abc"
b = "wxyz"
print(s.repeatedStringMatch(a, b))
