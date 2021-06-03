# 剑指 Offer 46.：把数字翻译成字符串
# 相似题：91.解码方法 numDecodings
class Solution:

    # def translateNum(self, num: int) -> int:
    #     y, x = 1, 1
    #     nums = str(num)
    #     for i in range(2, len(nums)+1):  # 相当于从 dp(2) 开始
    #         if '10' <= nums[i-2] + nums[i-1] <= '25':
    #             y, x = x+y, y
    #         else:
    #             x = y
    #     return y

    # dp[i]：到第 i 个字符串为止，所有翻译的方法个数为 dp。上楼梯。
    # def translateNum(self, num: int) -> int:
    #     nums = str(num)
    #     n = len(nums)
    #     dp = [0] * (n+1)
    #     dp[0], dp[1] = 1, 1
    #
    #     for i in range(2, len(nums)+1):
    #         if int(nums[i-2]) and int(nums[i-2] + nums[i-1]) <= 25:
    #             dp[i] = dp[i-1] + dp[i-2]
    #         else:
    #             dp[i] = dp[i-1]
    #     return dp[n]

    # def translateNum(self, num: int) -> int:
    #     s = str(num)
    #     a = b = 1
    #     for i in range(2, len(s) + 1):
    #         a, b = (a + b if "10" <= s[i - 2:i] <= "25" else a), a
    #     return a

    # def translateNum(self, num: int) -> int:
    #     s = str(num)
    #     n = len(s)
    #
    #     dp = [0] * (n+1)
    #     dp[0], dp[1] = 1, 1
    #     for i in range(2, n+1):
    #         if '10' <= s[i-2]+s[i-1] < '26':  # >= '10' 是为了避免比如 04 这样以 0 开头的数字。
    #             dp[i] = dp[i-1] + dp[i-2]
    #         else:
    #             dp[i] = dp[i-1]
    #     return dp[n]

    # def translateNum(self, num: int) -> int:
    #     x, y = 1, 1
    #     s = str(num)
    #     for i in range(2, len(s)+1):
    #         if '10' <= s[i-2] + s[i-1] < '26':
    #             y, x = x+y, y
    #         else:
    #             x = y
    #     return y

    def translateNum(self, num: int) -> int:
        nums = str(num)
        n = len(nums)
        dp = [1] * (n+1)
        for i in range(2, n+1):
            if '10' <= nums[i-2:i] <= '25':
                dp[i] = dp[i-1] + dp[i-2]
            else:
                dp[i] = dp[i-1]
        return dp[n]


s = Solution()
num = 12258
print(s.translateNum(num))

num = 506
print(s.translateNum(num))  # 结果：1种

num = 18822
print(s.translateNum(num))

num = 0
print(s.translateNum(num))
