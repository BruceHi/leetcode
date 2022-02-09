# 1716. 计算力扣银行的钱
class Solution:
    def totalMoney(self, n: int) -> int:
        week, day = n // 7, n % 7
        res = 0
        for i in range(week):
            for j in range(i+1, i+8):
                res += j
        res += sum(i+week+1 for i in range(day))
        return res

s = Solution()
n = 4
print(s.totalMoney(n))

n = 10
print(s.totalMoney(n))

n = 20
print(s.totalMoney(n))
