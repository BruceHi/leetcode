# 1185. 一周中的第几天
from datetime import datetime


class Solution:
    # def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
    #     names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #     dic = {i: v for i, v in enumerate(names)}
    #     d = datetime(year=year, month=month, day=day)
    #     # print(d.weekday())
    #     return dic[d.weekday()]

    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return datetime(year=year, month=month, day=day).strftime('%A')


s = Solution()
day = 31
month = 8
year = 2019
print(s.dayOfTheWeek(day, month, year))

day = 18
month = 7
year = 1999
print(s.dayOfTheWeek(day, month, year))

day = 15
month = 8
year = 1993
print(s.dayOfTheWeek(day, month, year))
