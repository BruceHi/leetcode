# 复原 ip 地址
from typing import List


class Solution:

    # def restoreIpAddresses(self, s: str) -> List[str]:
    #     res = []
    #     for a in range(1, 4):
    #         for b in range(1, 4):
    #             for c in range(1, 4):
    #                 for d in range(1, 4):
    #                     if a + b + c + d == len(s):
    #                         n1 = int(s[:a])
    #                         n2 = int(s[a:a+b])
    #                         n3 = int(s[a+b:a+b+c])
    #                         n4 = int(s[a+b+c:])
    #                         if n1 < 256 and n2 < 256 and n3 < 256 and n4 < 256:
    #                             ip = str(n1) + '.' + str(n2) + '.' + str(n3) + '.' + str(n4)
    #                             if len(ip) == len(s) + 3:
    #                                 res.append(ip)
    #     return res

    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    if i + j + k < n:
                        a = int(s[:i])
                        b = int(s[i:i+j])
                        c = int(s[i+j:i+j+k])
                        d = int(s[i+j+k:])
                        if a <= 255 and b <= 255 and c <= 255 and d <= 255:
                            ip = '.'.join(map(str, [a, b, c, d]))
                            if len(ip) == n + 3:
                                res.append(ip)
        return res

    # def restoreIpAddresses(self, s: str) -> List[str]:
    #     res = []
    #
    #     def dfs(cur, start):  # cur 划分的片段元组, start 开始统计的位置
    #
    #         if len(cur) == 4 and start == len(s):
    #             ip = '.'.join(cur)
    #             res.append(ip)
    #             return
    #
    #         if len(cur) > 4 or start >= len(s):
    #             return
    #
    #         # if s[start] == '0':
    #         #     dfs(cur + ['0'], start+1)
    #         #     return
    #
    #         for i in range(start+1, start + 4):
    #             tmp = s[start:i]
    #             if int(tmp) <= 255 and str(int(tmp)) == tmp:
    #                 dfs(cur + [tmp], i)
    #     dfs([], 0)
    #     return res

    # def restoreIpAddresses(self, s: str) -> List[str]:
    #     res = []
    #
    #     def dfs(cur, start):  # cur 划分的片段元组, start 开始统计的位置
    #
    #         if len(cur) == 4 and start == len(s):
    #             ip = '.'.join(cur)
    #             res.append(ip)
    #             return
    #
    #         if len(cur) > 4 or start >= len(s):
    #             return
    #
    #         if s[start] == '0':  # 对于 0 而言，不必拼接了
    #             dfs(cur + ['0'], start+1)
    #             return
    #
    #         for i in range(start+1, start + 4):  # 向后寻找包括自己在内的 3 个数进行验证
    #             tmp = s[start:i]
    #             if int(tmp) <= 255:
    #                 dfs(cur + [tmp], i)
    #
    #     dfs([], 0)
    #     return res



obj = Solution()
print(obj.restoreIpAddresses("25525511135"))

print(obj.restoreIpAddresses("0000"))

print(obj.restoreIpAddresses("1111"))

print(obj.restoreIpAddresses("010010"))

print(obj.restoreIpAddresses("101023"))

print(obj.restoreIpAddresses("000256"))