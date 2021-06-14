# 剑指 offer 13. 机器人的运动范围
# BFS 广度优先搜索
from collections import deque


class Solution:
    # def movingCount(self, m: int, n: int, k: int) -> int:
    #     def digit_sum(n):
    #         res = 0
    #         while n:
    #             res += n % 10
    #             n //= 10
    #         return res
    #
    #     queue = deque([(0, 0)])
    #     visited = set()
    #     while queue:
    #         x, y = queue.popleft()
    #         if (x, y) not in visited and 0 <= x < m and 0 <= y < n and digit_sum(x) + digit_sum(y) <= k:
    #             visited.add((x, y))
    #             queue.append((x+1, y))
    #             queue.append((x, y+1))
    #     return len(visited)

    # def movingCount(self, m: int, n: int, k: int) -> int:
    #     def digit_sum(n):
    #         res = 0
    #         while n:
    #             res += n % 10
    #             n //= 10
    #         return res
    #
    #     queue = deque([(0, 0)])
    #     record = set()
    #     while queue:
    #         x, y = queue.popleft()
    #         if 0 <= x < m and 0 <= y < n and (x, y) not in record and digit_sum(x) + digit_sum(y) <= k:
    #             record.add((x, y))
    #             queue.append((x+1, y))
    #             queue.append((x, y+1))
    #     return len(record)

    def movingCount(self, m: int, n: int, k: int) -> int:

        def digit_sum(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res

        queue = deque([(0, 0)])
        record = set()
        while queue:
            a, b = queue.popleft()
            if (a, b) not in record and 0 <= a < m and 0 <= b < n and digit_sum(a) + digit_sum(b) <= k:
                record.add((a, b))
                queue.append((a+1, b))
                queue.append((a, b+1))
                print(queue)
        print(record)
        return len(record)




s = Solution()
m = 2
n = 3
k = 1
print(s.movingCount(m, n, k))

m = 3
n = 1
k = 0
print(s.movingCount(m, n, k))

m = 1
n = 2
k = 1
print(s.movingCount(m, n, k))

m = 3
n = 2
k = 17
print(s.movingCount(m, n, k))

m = 16
n = 16
k = 2
print(s.movingCount(m, n, k))
