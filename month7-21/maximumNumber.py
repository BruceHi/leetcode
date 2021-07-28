from typing import List


class Solution:
    # def maximumNumber(self, num: str, change: List[int]) -> str:
    #     res = ''
    #     for c in num:
    #         v = int(c)
    #         if v < change[v]:
    #             res += str(change[v])
    #         else:
    #             res += c
    #     return res

    # 超时
    # def maximumNumber(self, num: str, change: List[int]) -> str:
    #     res = ''
    #     nums = []
    #     for i, c in enumerate(num):
    #         v = int(c)
    #         if v <= change[v]:
    #             res += str(change[v])
    #         else:
    #             nums.append(res[:i] + num[i:])
    #             res = num[:i+1]
    #     if int(num[-1]) <= change[int(num[-1])]:
    #         nums.append(res)
    #     return max(nums)

    # def maximumNumber(self, num: str, change: List[int]) -> str:
    #     tmp = ''
    #     res = ''
    #     for i, c in enumerate(num):
    #         v = int(c)
    #         if v <= change[v]:
    #             tmp += str(change[v])
    #         else:
    #             res = max(tmp[:i] + num[i:], res)
    #             tmp = num[:i+1]
    #
    #     if int(num[-1]) <= change[int(num[-1])]:
    #         res = max(res, tmp)
    #
    #     return res

    def maximumNumber(self, num: str, change: List[int]) -> str:
        res = ''
        for i, c in enumerate(num):
            v = int(c)
            if v <= change[v]:
                res += str(change[v])
            else:
                return res[:i] + num[i:]

        if int(num[-1]) <= change[int(num[-1])]:
            return res

        return res


s = Solution()
num = "132"
change = [9,8,5,0,3,6,4,2,6,8]
print(s.maximumNumber(num, change))

num = "021"
change = [9,4,3,5,7,2,1,9,0,6]
print(s.maximumNumber(num, change))

num = "5"
change = [1,4,7,5,3,2,5,6,9,4]
print(s.maximumNumber(num, change))

num = "214010"
change = [6,7,9,7,4,0,3,4,4,7]
print(s.maximumNumber(num, change))

num = "0"
change = [0,1,4,6,7,5,2,4,8,9]
print(s.maximumNumber(num, change))

