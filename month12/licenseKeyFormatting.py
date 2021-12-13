# 482. 密钥格式化
class Solution:
    # def licenseKeyFormatting(self, s: str, k: int) -> str:
    #     s = s.replace('-', '').upper()[::-1]
    #     res = ''
    #     for i in range(0, len(s), k):
    #         res += '-' + s[i:i+k]
    #     return res[1:][::-1]

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace('-', '').upper()[::-1]
        # return [s[i:i+k] for i in range(0, len(s), k)]
        return '-'.join(s[i:i+k] for i in range(0, len(s), k))[::-1]


obj = Solution()
S = "5F3Z-2e-9-w"
K = 4
print(obj.licenseKeyFormatting(S, K))

S = "2-5g-3-J"
K = 2
print(obj.licenseKeyFormatting(S, K))
