# 633. 平方数之和
from math import sqrt


class Solution:
    # def judgeSquareSum(self, c: int) -> bool:
    #     nums = [x*x for x in range(int(sqrt(c))+1)]
    #     set_nums = set(nums)
    #     for num in nums:
    #         if c-num in set_nums:
    #             return True
    #     return False

    # 双指针
    # def judgeSquareSum(self, c: int) -> bool:
    #     left, right = 0, int(sqrt(c))
    #     while left <= right:  # 值可以取相同的
    #         num = left ** 2 + right ** 2
    #         if num == c:
    #             return True
    #         if num < c:
    #             left += 1
    #         else:
    #             right -= 1
    #     return False

    def judgeSquareSum(self, c: int) -> bool:
        nums = set(x*x for x in range(int(sqrt(c))+1))
        for num in nums:
            if c - num in nums:
                return True
        return False


s = Solution()
c = 5
print(s.judgeSquareSum(c))

c = 3
print(s.judgeSquareSum(c))

c = 4
print(s.judgeSquareSum(c))

c = 2
print(s.judgeSquareSum(c))

c = 1
print(s.judgeSquareSum(c))

c = 0
print(s.judgeSquareSum(c))
