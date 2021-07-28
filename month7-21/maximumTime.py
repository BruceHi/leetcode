# 1736. 替换隐藏数字得到的最晚时间
class Solution:
    # 最大取值是 23：59，后两位根本达不到 60
    # def maximumTime(self, time: str) -> str:
    #     a, b, c, d = ['2', '1'], ['9', '3'], ['6', '5'], ['9', '0']
    #     res = ''
    #     if time[0] == "?" and time[1] == '?':
    #         res += '23'
    #     elif time[0] == "?":
    #         if a[0] + time[1] < '24':
    #             res += a[0] + time[1]
    #         else:
    #             res += a[1] + time[1]
    #     elif time[1] == '?':
    #         if time[0] + b[0] < '24':
    #             res += time[0] + b[0]
    #         else:
    #             res += time[0] + b[1]
    #     else:
    #         res += time[0:2]
    #     res += ':'
    #
    #     if time[3] == "?" and time[4] == '?':
    #         res += '59'
    #     elif time[3] == "?":
    #         if c[0] + time[4] < '60':
    #             res += c[0] + time[4]
    #         else:
    #             res += c[1] + time[4]
    #     elif time[4] == '?':
    #         if time[3] + d[0] < '60':
    #             res += time[3] + d[0]
    #         else:
    #             res += time[3] + d[1]
    #     else:
    #         res += time[3:5]
    #
    #     return res

    def maximumTime(self, time: str) -> str:
        times = list(time)
        if times[0] == '?':
            if '4' <= times[1] <= '9':  # 必须 有 <= '9'，因为我们还要考虑 ‘？’
                times[0] = '1'
            else:
                times[0] = '2'

        # 此时times[0] 肯定有数值
        if times[1] == '?':
            if times[0] == '2':
                times[1] = '3'
            else:
                times[1] = '9'

        if times[3] == '?':
            times[3] = '5'
        if times[4] == '?':
            times[4] = '9'

        return ''.join(times)


s = Solution()
time = "2?:?0"
print(s.maximumTime(time))

time = "0?:3?"
print(s.maximumTime(time))

time = "1?:22"
print(s.maximumTime(time))

time = "00:??"
print(s.maximumTime(time))