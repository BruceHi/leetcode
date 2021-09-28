# 600. 不含连续1 的非负整数
# 包括 0
class Solution:
    # 超时
    # def findIntegers(self, n: int) -> int:
    #     res = n + 1
    #     for i in range(n+1):
    #         b = bin(i)
    #         for j in range(len(b)-1):
    #             if b[j] == b[j+1] == '1':
    #                 res -= 1
    #                 break  # 不break 容易出现 '1111' 的情况进行多次统计
    #     return res

    def findIntegers(self, n: int) -> int:
        res = 0
        for i in range(n+1):
            if '11' not in bin(i):
                res += 1
        return res


s = Solution()
print(s.findIntegers(5))

print(s.findIntegers(7))


# a = 0b101
# print(a)
# print(type(a))
