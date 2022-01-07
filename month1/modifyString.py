# 1576. 替换所有的问号
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        for i, c in enumerate(s):
            if s[i] == '?':
                for new in 'abc':
                    if not (i > 0 and new == s[i-1] or i < len(s)-1 and new == s[i+1]):
                        s[i] = new
                        break
        return ''.join(s)



obj = Solution()
s = "?zs"
print(obj.modifyString(s))

s = "ubv?w"
print(obj.modifyString(s))

s = "j?qg??b"
print(obj.modifyString(s))

s = "??yw?ipkj?"
print(obj.modifyString(s))
