class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ''
        for i, c in enumerate(s):
            if i & 1:
                res += chr(ord(s[i-1]) + int(c))
            else:
                res += c
        return res


obj = Solution()
s = "a1c1e1"
print(obj.replaceDigits(s))

s = "a1b2c3d4e"
print(obj.replaceDigits(s))

print(ord('c'))
print(chr(99))