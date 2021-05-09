from typing import List
class Solution:
    # 错误
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        if len(logs) == 1:
            return logs[0][0]
        logs.sort()
        record = [logs[0][0], 1]
        dist = []  # 重叠区间
        for a, b in logs:
            if not dist or a > dist[0][1]:
                dist = [[a, b], 1]
            else:
                dist[0] = [a, min(dist[0][1], b)]
                dist[1] += 1
            if dist[1] > record[1]:
                record = [dist[0][0], dist[1]]
        return record[0]



s = Solution()
logs = [[1993,1999],[2000,2010]]
print(s.maximumPopulation(logs))

logs = [[1950,1961],[1960,1971],[1970,1981]]
print(s.maximumPopulation(logs))

logs = [[2033,2034],[2039,2047],[1998,2042],[2047,2048],[2025,2029],[2005,2044],[1990,1992],[1952,1956],[1984,2014]]
print(s.maximumPopulation(logs))