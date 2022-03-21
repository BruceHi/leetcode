# 91.解码方法
# 相似题：剑指 Offer 46.：把数字翻译成字符串 translateNum
# 46 题是肯定可以有对应的字符串的，而本题有可能无法解码，返回 0，比如含前导的如 1002
class Solution:
    # def numDecodings(self, s: str) -> int:
    #     if s.startswith('0'):
    #         return 0
    #
    #     n = len(s)
    #     dp = [0] * (n+1)
    #     dp[0], dp[1] = 1, 1
    #
    #     for i in range(2, n+1):
    #         # and 优先级要高于 or
    #         if s[i-1] == '0' and (s[i-2] > '2' or s[i-2] == '0'):
    #             return 0
    #         if s[i-2] == '0' or s[i-2:i] > '26':
    #             dp[i] = dp[i-1]
    #         elif s[i-1] != '0':
    #             dp[i] = dp[i-1] + dp[i-2]
    #         else:
    #             dp[i] = dp[i-2]
    #     return dp[n]

    # # 前两种方法，dp 表示前 i 个字符串可以解码的总个数
    # 都说前 i 个已经可以解码了，还要判断前 i 个能不能解码，感觉有些不合适。
    # 更正确的表述是：若前 i 个字符串可以解码，dp 表示前 i 个字符串可以解码的总个数
    # def numDecodings(self, s: str) -> int:
    #     if s.startswith('0'):
    #         return 0
    #
    #     n = len(s)
    #     dp = [1] * (n+1)
    #
    #     for i in range(2, n+1):
    #         if s[i-1] == '0' and s[i-2] not in '12':  # 还真不能用 not
    #             return 0
    #         if s[i-2:i] in ['10', '20']:  # 只有组合在一起才行
    #             dp[i] = dp[i-2]
    #         elif '10' < s[i-2:i] <= '26':
    #             dp[i] = dp[i-1] + dp[i-2]
    #         else:  # '01'到 ‘09’ 或 > '26'
    #             dp[i] = dp[i-1]
    #     return dp[n]

    # 以列举 可能出现的字符作为 dp，会有四种结果：0， dp[i-1], dp[i-2], dp[i-1] + dp[i-2]
    # ‘00’， ‘01’~‘09’， ‘10’，‘11’~‘19’ ‘20’， ‘21’~‘26’， >'26'
    # def numDecodings(self, s: str) -> int:
    #     if s.startswith('0'):
    #         return 0
    #
    #     n = len(s)
    #     dp = [1] * (n+1)
    #
    #     for i in range(2, n+1):
    #         if s[i-1] == '0' and s[i-2] not in '12':
    #             return 0
    #         if s[i-2:i] in ['10', '20']:
    #             dp[i] = dp[i-2]
    #         elif '10' < s[i-2:i] <= '26':  # 已经剔除了 '20'
    #             dp[i] = dp[i-1] + dp[i-2]
    #         else:
    #             dp[i] = dp[i-1]
    #     return dp[n]


    # def numDecodings(self, s: str) -> int:
    #     if s.startswith('0'):
    #         return 0
    #     n = len(s)
    #     dp = [1] * (n+1)
    #     for i in range(2, n+1):
    #         if s[i-1] == '0' and s[i-2] not in '12':
    #             return 0
    #         if s[i-2:i] in ['10', '20']:
    #             dp[i] = dp[i-2]
    #         elif '10' < s[i-2:i] <= '26':
    #             dp[i] = dp[i-1] + dp[i-2]
    #         else:
    #             dp[i] = dp[i-1]
    #     return dp[n]

    # def numDecodings(self, s: str) -> int:
    #     s = '0' + s
    #     n = len(s)
    #     dp = [1] * n
    #     for i in range(1, n):
    #         if s[i-1:i+1] in ['10', '20']:
    #             dp[i] = dp[i-2]
    #         elif '10' < s[i-1:i+1] <= '26':
    #             dp[i] = dp[i-1] + dp[i-2]
    #         elif '01' <= s[i-1:i+1] <= '09' or s[i] != '0' and s[i-1:i+1] > '26':
    #             dp[i] = dp[i-1]
    #         else:
    #             return 0
    #     return dp[n-1]

    # 官方题解，看起来更为简洁
    # 只分为 2 种情况，可以单独的，可以组合的
    # dp[i] = dp[i-1](单独，否则为 0) + dp[i-2](结合，否则为 0)
    # def numDecodings(self, s: str) -> int:
    #     n = len(s)
    #     dp = [1] + [0] * n
    #     for i in range(1, n+1):
    #         if s[i-1] != '0':  # 至少 1 种解法
    #             dp[i] += dp[i-1]
    #         if i > 1 and s[i-2] != '0' and s[i-2:i] <= '26':
    #             dp[i] += dp[i-2]
    #     return dp[n]

    # def numDecodings(self, s: str) -> int:
    #     if s.startswith('0'):
    #         return 0
    #     n = len(s)
    #     dp = [0] * (n+1)
    #     dp[0] = dp[1] = 1
    #     for i in range(2, n+1):
    #         c = s[i-2:i]
    #         if c[1] == '0':
    #             if c in ['10', '20']:
    #                 dp[i] = dp[i - 2]
    #             else:
    #                 return 0
    #         elif '01' <= c <= '09' or c > '26':
    #             dp[i] = dp[i-1]
    #         else:
    #             dp[i] = dp[i-1] + dp[i-2]
    #     return dp[n]

    def numDecodings(self, s: str) -> int:
        if s.startswith('0'):
            return 0

        n = len(s)
        dp = [0] * (n+1)
        dp[0] = dp[1] = 1
        for i in range(2, n+1):
            if s[i-1] != '0':
                dp[i] = dp[i-1]
            if '10' <= s[i-2:i] <= '26':
                dp[i] += dp[i-2]  # 注意这点
        return dp[n]


obj = Solution()
s = "12"
print(obj.numDecodings(s))

s = "226"
print(obj.numDecodings(s))

s = "0"
print(obj.numDecodings(s))  # 输出 0

s = "1"
print(obj.numDecodings(s))

s = "2"
print(obj.numDecodings(s))

s = "12901"
print(obj.numDecodings(s))  # 返回 0，不能解码

s = "200"
print(obj.numDecodings(s))

s = "2101"
print(obj.numDecodings(s))  # 输出 1

s = "10"
print(obj.numDecodings(s))  # 输出 1

# 正确结果
# 2
# 3
# 0
# 1
# 1
# 0
# 0
# 1
# 1