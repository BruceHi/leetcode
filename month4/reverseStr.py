# 541. 反转字符串 2
class Solution:
    # def reverseStr(self, s: str, k: int) -> str:
    #     res = ''
    #     t = 0
    #     for i in range(0, len(s), k):
    #         if not t & 1:
    #             res += s[i:i+k][::-1]
    #         else:
    #             res += s[i:i+k]
    #         t += 1
    #     return res


    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        for i in range(0, len(s), 2 * k):
            t[i:i+k] = reversed(t[i:i+k])
        return ''.join(t)


obj = Solution()
s = "abcdefg"
k = 2
print(obj.reverseStr(s, k))

s = "abcd"
k = 2
print(obj.reverseStr(s, k))

