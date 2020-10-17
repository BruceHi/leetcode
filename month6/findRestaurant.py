# 两个列表的最小索引总和
from typing import List


class Solution:
    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    #     dic, record = {}, {}
    #     for i, s in enumerate(list1):
    #         dic[s] = i
    #     for i, s in enumerate(list2):
    #         if s in dic:
    #             record[s] = dic[s] + i
    #     # return [min(res, key=res.get)]  # 返回最小键值所对应的键，若有好几个最小的，只返回第一个，所以不和题意。
    #     res = []
    #     for key, val in record.items():
    #         if val == min(record.values()):
    #             res.append(key)
    #     return res

    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    #     dic = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
    #     return [x for x in dic if dic[x] == min(dic.values())]

    # def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
    #     dic, record = {}, {}
    #     for i, s in enumerate(list1):
    #         dic[s] = i
    #     for i, s in enumerate(list2):
    #         if s in dic:
    #             record[s] = dic[s] + i
    #     res = []
    #     for key, val in record.items():
    #         if val == min(record.values()):
    #             res.append(key)
    #     return res

    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dic = {x: list1.index(x) + list2.index(x) for x in set(list1) & set(list2)}
        return [x for x in dic if dic[x] == min(dic.values())]




s = Solution()
a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
b = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
print(s.findRestaurant(a, b))

a = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
b = ["KFC", "Shogun", "Burger King"]
print(s.findRestaurant(a, b))

a = ["Shogun","Tapioca Express","Burger King","KFC"]
b = ["KFC","Burger King","Tapioca Express","Shogun"]
print(s.findRestaurant(a, b))
