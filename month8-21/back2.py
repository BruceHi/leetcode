# 0-1 背包问题
# 对于一组不同重量、不可分割的物品，我们需要选择一些装入背包，
# 在满足背包最大重量限制的前提下，背包中物品总重量的最大值是多少呢？
# 只含 w 和 target

class Solution:
    # 错误，初始值不对
    # def knapsack(self, nums, target):
    #     n = len(nums)
    #     dp = [[False] * (target+1) for _ in range(1+n)]
    #     for i in range(1, n+1):
    #         num = nums[i-1]
    #         for j in range(target+1):
    #             if j > num:
    #                 dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
    #             else:
    #                 dp[i][j] = dp[i - 1][j]
    #     print(dp)
    #     for j in range(target, -1, -1):
    #         if dp[n][j]:
    #             return j
    #     return 0

    # $dp[i][j]$ 表示从数组的 $[0, i]$ 这个子区间内挑选一些正整数，每个数只能用一次，
    # 是否和等于 $j$，结果为 `True` 或者 `False`
    # def knapsack(self, nums, target):
    #     n = len(nums)
    #     dp = [[False] * (target+1) for _ in range(n)]
    #     dp[0][0] = dp[0][nums[0]] = True  # 注意与普通的 0-1 背包区别
    #
    #     for i in range(1, n):
    #         num = nums[i]
    #         for j in range(target+1):
    #             if j >= num:
    #                 dp[i][j] = dp[i-1][j] or dp[i-1][j-num]
    #             else:
    #                 dp[i][j] = dp[i-1][j]  # 直接拉下来
    #         print(dp[i])
    #
    #     for j in range(target, -1, -1):
    #         if dp[n-1][j]:
    #             return j
    #
    #     return 0

    # 矩阵压缩
    # def knapsack(self, nums, target):
    #     n = len(nums)
    #     dp = [False] * (target+1)
    #     dp[0] = dp[nums[0]] = True
    #
    #     for i in range(1, n):
    #         for j in range(target, nums[i]-1, -1):
    #             dp[j] = dp[j] or dp[j-nums[i]]
    #         print(dp)
    #
    #     for j in range(target, -1, -1):
    #         if dp[j]:
    #             return j

    def knapsack(self, nums, target):
        n = len(nums)
        dp = [True] + [False] * target

        for i in range(n):
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]
            print(dp)

        for j in range(target, -1, -1):
            if dp[j]:
                return j


s = Solution()
nums = [2, 2, 4, 6, 3]
target = 9
print(s.knapsack(nums, target))
