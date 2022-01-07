# 1154. 一年中的第几天
from datetime import datetime


class Solution:
    # def dayOfYear(self, date: str) -> int:
    #     t_end = datetime.strptime(date, '%Y-%m-%d')
    #     t_start = datetime(year=t_end.year, day=1, month=1)
    #     return (t_end - t_start).days + 1

    def dayOfYear(self, date: str) -> int:
        t = datetime.strptime(date, '%Y-%m-%d').strftime('%j')
        return int(t)


s = Solution()
date = "2019-01-09"
print(s.dayOfYear(date))

date = "2019-02-10"
print(s.dayOfYear(date))

date = "2003-03-01"
print(s.dayOfYear(date))

date = "2021-12-21"
print(s.dayOfYear(date))
