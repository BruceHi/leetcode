# 441. 排列硬币
# 二分查找 逆向
class Solution:
    # def arrangeCoins(self, n: int) -> int:
    #     pre_sum = 0
    #     i = 0
    #     while pre_sum <= n:
    #         i += 1
    #         pre_sum += i
    #     return i-1

    def arrangeCoins(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) // 2
            if mid * (mid + 1) <= 2 * n:
                left = mid
            else:
                right = mid - 1
        return left



s = Solution()
print(s.arrangeCoins(1))

print(s.arrangeCoins(3))

print(s.arrangeCoins(5))

print(s.arrangeCoins(8))
