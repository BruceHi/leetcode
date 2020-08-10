# 复原 ip 地址
from typing import List


class Solution:
    # def restoreIpAddresses(self, s: str) -> List[str]:
    #     res = []
    #
    #     def dsf(s, t, cur):  # s: 剩余要复原的，t: 已经拼凑的东西
    #         if not s and cur == 4:
    #             res.append(t)
    #             return
    #         if s[0] == '0':
    #             dsf(s[1:], t+'.0', cur+1)
    #         for i in range(1, 4):
    #             if int(s[0: i]) <= 255:
    #                 dsf(s[i:], t+s[0:i], cur+1)
    #     dsf(s, '', 0)
    #     return res

    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        for a in range(1, 4):
            for b in range(1, 4):
                for c in range(1, 4):
                    for d in range(1, 4):
                        if a + b + c + d == len(s):
                            n1 = int(s[:a])
                            n2 = int(s[a:a+b])
                            n3 = int(s[a+b:a+b+c])
                            n4 = int(s[a+b+c:])
                            if n1 < 256 and n2 < 256 and n3 < 256 and n4 < 256:
                                ip = str(n1) + '.' + str(n2) + '.' + str(n3) + '.' + str(n4)
                                if len(ip) == len(s) + 3:
                                    res.append(ip)
        return res


obj = Solution()
print(obj.restoreIpAddresses("25525511135"))