# 821. 字符的最短距离
from typing import List


class Solution:
    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     nums = []
    #     for i, a in enumerate(s):
    #         if a == c:
    #             nums.append(i)
    #
    #     res = []
    #     for i in range(len(s)):
    #         res.append(min(abs(num - i) for num in nums))
    #     return res

    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     nums = []
    #     for i, t in enumerate(s):
    #         if t == c:
    #             nums.append(i)
    #
    #     res = []
    #     for i in range(len(s)):
    #         res.append(min(abs(i-num) for num in nums))
    #     return res

    # 两次遍历
    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     res = []
    #
    #     # 到左边的最小距离
    #     idx = -float('inf')
    #     for i, t in enumerate(s):
    #         if t == c:
    #             idx = i
    #         res.append(i - idx)
    #
    #     # 到右边的最小距离，注意初始值idx 的选取
    #     idx = float('inf')
    #     for i in range(len(s)-1, -1, -1):
    #         if s[i] == c:
    #             idx = i
    #         res[i] = min(res[i], idx-i)  # 注意方向
    #
    #     return res

    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     res = []
    #
    #     idx = float('-inf')
    #     for i, t in enumerate(s):
    #         if t == c:
    #             idx = i
    #         res.append(i-idx)
    #
    #     idx = float('inf')
    #     for i in range(len(s)-1, -1, -1):
    #         if s[i] == c:
    #             idx = i
    #         res[i] = min(res[i], idx-i)
    #
    #     return res

    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     res = []
    #
    #     idx = float('-inf')
    #     for i, t in enumerate(s):
    #         if t == c:
    #             idx = i
    #         res.append(i-idx)
    #
    #     idx = float('inf')
    #     for i in range(len(s)-1, -1, -1):
    #         if s[i] == c:
    #             idx = i
    #         res[i] = min(res[i], idx-i)
    #
    #     return res

    # def shortestToChar(self, s: str, c: str) -> List[int]:
    #     res = []
    #
    #     start = float('-inf')
    #     for i, t in enumerate(s):
    #         if t == c:
    #             start = i
    #         res.append(i-start)
    #
    #     start = float('inf')
    #     for i in range(len(s)-1, -1, -1):
    #         if s[i] == c:
    #             start = i
    #         res[i] = min(res[i], start-i)
    #     return res

    def shortestToChar(self, s: str, c: str) -> List[int]:
        res = []
        last = float('-inf')
        for i, t in enumerate(s):
            if t == c:
                last = i
            res.append(i - last)

        last = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                last = i
            res[i] = min(res[i], last-i)
        return res


obj = Solution()
s = "loveleetcode"
c = "e"
print(obj.shortestToChar(s, c))

s = "aaab"
c = "b"
print(obj.shortestToChar(s, c))
