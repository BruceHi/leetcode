# 1436. 旅行终点站
from typing import List


class Solution:
    # def destCity(self, paths: List[List[str]]) -> str:
    #
    #     def next_index(i):
    #         for j, (a, _) in enumerate(paths):
    #             if paths[i][1] == a:
    #                 return j
    #         return -1
    #
    #     i = 0
    #     while next_index(i) != -1:
    #         i = next_index(i)
    #     return paths[i][1]

    # def destCity(self, paths: List[List[str]]) -> str:
    #     citiesA = {path[0] for path in paths}
    #     # return [path[1] for path in paths if path[1] not in citiesA][0]
    #     # 只含一个元素，可以使用 next 迭代出来，牛逼
    #     return next(path[1] for path in paths if path[1] not in citiesA)

    def destCity(self, paths: List[List[str]]) -> str:
        city_set = {path[0] for path in paths}
        for _, b in paths:
            if b not in city_set:
                return b


s = Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(s.destCity(paths))

paths = [["B","C"],["D","B"],["C","A"]]
print(s.destCity(paths))

paths = [["A","Z"]]
print(s.destCity(paths))
