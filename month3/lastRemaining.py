# 剑指 offer 62.圆圈中最后剩下的数字


class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = list(range(n))
        i = (m-1) % n
        while len(nums) != 1:
            nums.pop(i)
            i = (i-1+m) % len(nums)
        return nums[0]

s = Solution()
n = 5
m = 3
print(s.lastRemaining(n, m))

n = 10
m = 17
print(s.lastRemaining(n, m))
