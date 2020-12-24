# 剑指 offer 58-2.左旋转字符串
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]


obj = Solution()
s = "abcdefg"
k = 2
print(obj.reverseLeftWords(s, k))

s = "lrloseumgh"
k = 6
print(obj.reverseLeftWords(s, k))
