# 89. 格雷编码
from typing import List


class Solution:
    # def grayCode(self, n: int) -> List[int]:
    #     if not n:
    #         return [0]
    #     res = []
    #
    #     # set 是无序的，不能用 set，要求结果必须是有序的
    #     def dfs(start, cur):
    #         if start in cur:
    #             return
    #         if len(cur) == 2**n-1:
    #             cur.append(start)
    #             res.append(cur)
    #             return
    #         for i in range(n):
    #             dfs(start[:i] + str(int(start[i] == '0')) + start[i+1:], cur + [start])
    #             if len(res) == 1:
    #                 return
    #
    #     dfs('0'*n, [])
    #     return [int(x, base=2) for x in res[0] if x]

    # 格雷姆等于 值异或（向右移位）
    # 1与空异或还是得 1，0 与 空异或为 0。空可以看成 0.
    # 移位的优先级大于与，或，异或
    # def grayCode(self, n: int) -> List[int]:
    #     return [i ^ i >> 1 for i in range(2**n)]

    # def grayCode(self, n: int) -> List[int]:
    #     return [i ^ (i >> 1) for i in range(1 << n)]

    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]


s = Solution()
print(s.grayCode(2))

print(s.grayCode(0))
