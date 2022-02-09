# 1342. 将数字变为 0 的操作次数
class Solution:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            if num & 1:
                num -= 1
            else:
                num //= 2
            res += 1
        return res


s = Solution()
num = 14
print(s.numberOfSteps(num))

num = 8
print(s.numberOfSteps(num))

num = 123
print(s.numberOfSteps(num))

num = 10 ** 6
print(s.numberOfSteps(num))
