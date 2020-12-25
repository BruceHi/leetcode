# 面试题 01.06.字符串压缩
class Solution:
    def compressString(self, S: str) -> str:
        if not S:
            return ''
        res = ''
        i = 0
        n = len(S)
        for j, c in enumerate(S):
            if c != S[i]:
                res += S[i] + str(j-i)
                i = j
        res += S[-1] + str(n-i)
        return res if len(res) < n else S


obj = Solution()
print(obj.compressString("aabcccccaaa"))

print(obj.compressString("abbccd"))

print(obj.compressString(""))
