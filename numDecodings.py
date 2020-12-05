# 91.解码方法
# 相似题：剑指 Offer 46.：把数字翻译成字符串 translateNum
# 46 题是肯定可以有对应的字符串的，而本题有可能无法解码，返回 0，比如含前导的如 1002
class Solution:
    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 1

        for i in range(2, n+1):
            # and 优先级要高于 or
            if s[i-1] == '0' and (s[i-2] > '2' or s[i-2] == '0'):
                return 0
            if s[i-2] == '0' or s[i-2:i] > '26':
                dp[i] = dp[i-1]
            elif s[i-1] != '0':
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-2]
        return dp[n]



obj = Solution()
s = "12"
print(obj.numDecodings(s))

s = "226"
print(obj.numDecodings(s))

s = "0"
print(obj.numDecodings(s))

s = "1"
print(obj.numDecodings(s))

s = "2"
print(obj.numDecodings(s))

s = "12901"
print(obj.numDecodings(s))  # 返回 0，不能解码

s = "200"
print(obj.numDecodings(s))

s = "2101"
print(obj.numDecodings(s))