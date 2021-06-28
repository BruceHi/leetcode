class Solution:
    # 错误
    # def numberOfRounds(self, startTime: str, finishTime: str) -> int:
    #     if startTime[:2] == finishTime[:2]:
    #         count = 0
    #         for x in ['00', '15', '30', '45']:
    #             if startTime[3:] <= x <= finishTime[3:]:
    #                 count += 1
    #         return count - 1
    #
    #     if int(finishTime[:2]) - int(startTime[:2]) == 1:
    #         first = 0
    #         for x in ['00', '15', '30', '45']:
    #             if startTime[3:] <= x <= '45':
    #                 first += 1
    #
    #         end = -1
    #         for x in ['00', '15', '30', '45']:
    #             if finishTime[3:] <= x <= '45':
    #                 end += 1
    #         return first + end

    # 错误
    # def numberOfRounds(self, startTime: str, finishTime: str) -> int:
    #     res = []
    #     for a in range(int(startTime[:2]), int(finishTime[:2])+1):
    #         for x in [0, 15, 30, 45]:
    #             b = int(finishTime[3:])+1 if int(finishTime[3:]) != 0 else 46
    #             if x in range(int(startTime[3:]), b):
    #                 res.append([a, x])
    #     return res

    # 转换思路，转换为分钟
    def numberOfRounds(self, startTime: str, finishTime: str) -> int:
        t1 = 60 * int(startTime[:2]) + int(startTime[3:])
        t2 = 60 * int(finishTime[:2]) + int(finishTime[3:])
        if t2 < t1:
            t2 += 1440
        t2 = t2 // 15 * 15
        return max(0, t2-t1) // 15


s = Solution()
startTime = "12:01"
finishTime = "12:44"
print(s.numberOfRounds(startTime, finishTime))

startTime = "12:01"
finishTime = "12:14"
print(s.numberOfRounds(startTime, finishTime))

startTime = "20:00"
finishTime = "06:00"
print(s.numberOfRounds(startTime, finishTime))

startTime = "00:00"
finishTime = "23:59"
print(s.numberOfRounds(startTime, finishTime))

startTime = "05:42"
finishTime = "06:37"
print(s.numberOfRounds(startTime, finishTime))

startTime = "20:00"
finishTime = "20:37"
print(s.numberOfRounds(startTime, finishTime))

startTime = "20:37"
finishTime = "21:00"
print(s.numberOfRounds(startTime, finishTime))

startTime = "05:00"
finishTime = "06:00"
print(s.numberOfRounds(startTime, finishTime))
