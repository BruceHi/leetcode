# 剑指 offer 49. 丑数
class Solution:
    # 超时
    # def nthUglyNumber(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     nums = [1]
    #     i = 0
    #     while i < n-1:
    #         min_val = float('inf')
    #         for num in nums:
    #             if nums[-1] < num * 2 < min_val:
    #                 min_val = num * 2
    #             if nums[-1] < num * 3 < min_val:
    #                 min_val = num * 3
    #             if nums[-1] < num * 5 < min_val:
    #                 min_val = num * 5
    #         nums.append(min_val)
    #         i += 1
    #     return nums[-1]

    # 动态规划
    # dp[i]：表示第 i 个丑数
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[1] = 1
        a, b, c = 1, 1, 1
        for i in range(2, n+1):
            n2, n3, n5 = dp[a] * 2, dp[b] * 3, dp[c] * 5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[n]


s = Solution()
n = 10
print(s.nthUglyNumber(n))
