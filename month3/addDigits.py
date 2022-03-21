# 258. 各位相加
class Solution:
    def addDigits(self, num: int) -> int:
        def get_nums(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res
        if num < 10:
            return num
        res = get_nums(num)
        while res >= 10:
            res = get_nums(res)
        return res


s = Solution()
num = 38
print(s.addDigits(num))

num = 0
print(s.addDigits(num))