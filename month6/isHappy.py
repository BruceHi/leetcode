# 快乐数
class Solution:
    # def isHappy(self, n: int) -> bool:
    #     record = set()
    #     while n != 1:
    #         res = 0
    #         while n:
    #             res += (n % 10) ** 2
    #             n //= 10
    #         n = res
    #         if n in record:
    #             return False
    #         record.add(n)
    #     return True

    def isHappy(self, n: int) -> bool:
        record = set()
        while n != 1:
            tmp = 0
            while n:
                tmp += (n % 10) ** 2
                n //= 10
            if tmp in record:
                return False
            n = tmp
            record.add(n)
        return True


s = Solution()
print(s.isHappy(19))

print(s.isHappy(2))
