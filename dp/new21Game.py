class Solution:
    # def new21Game(self, N: int, K: int, W: int) -> float:
    #     dp = [0.0] * (K+W)
    #     for i in range(K, N+1):
    #         dp[i] = 1
    #
    #     # for i in range(K-1, -1, -1):
    #     #     tmp = 0
    #     #     for j in range(W):
    #     #         tmp += dp[i+j+1]  # dx= (dx+1……dx+w) / W
    #     #     dp[i] = tmp / W  # 初始值必须为 float, 否则会警告。
    #
    #     for i in range(K-1, -1, -1):
    #         for j in range(W):
    #             dp[i] += dp[i+j+1] / W   # 对于第一个例子，上述结果为 1，这次为 0.999999999999
    #
    #     return dp[0]


    def new21Game(self, N: int, K: int, W: int) -> float:
        dp = [0.0] * (K+W)
        for i in range(K, min(N+1, K+W)):
            dp[i] = 1

        S = min(N - K + 1, W)
        for i in range(K-1, -1, -1):
            dp[i] = S / W
            S += dp[i] - dp[i+W]  # f(x-1) = (wf(x) - f(x+2) + f(x)) / W

        return dp[0]


s = Solution()
N = 10
K = 1
W = 10
print(s.new21Game(N, K, W))


N = 6
K = 1
W = 10
print(s.new21Game(N, K, W))

N = 21
K = 17
W = 10
print(s.new21Game(N, K, W))
