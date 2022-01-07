# 剑指 offer 62.圆圈中最后剩下的数字


class Solution:
    # 竟然超时了
    # def lastRemaining(self, n: int, m: int) -> int:
    #     nums = list(range(n))
    #     i = (m-1) % n
    #     while len(nums) != 1:
    #         nums.pop(i)
    #         i = (i-1+m) % len(nums)
    #     return nums[0]


    # 递归
    def lastRemaining(self, n: int, m: int) -> int:
        def f(n, m):
            if n == 0:
                return 0
            x = f(n-1, m)
            return (x + m) % n

        return f(n, m)


s = Solution()
n = 5
m = 3
print(s.lastRemaining(n, m))

n = 10
m = 17
print(s.lastRemaining(n, m))
