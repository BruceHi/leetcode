# 字母异位词分组
from typing import List
from collections import defaultdict
from collections import Iterable
import collections


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     dic = {}
    #     for s in strs:
    #         tmp = ''.join(sorted(s))
    #         if tmp in dic:
    #             dic[tmp].append(s)
    #         else:
    #             dic[tmp] = [s]
    #
    #     # return [_ for _ in dic.values()]
    #     return list(dic.values())

    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     dic = defaultdict(list)
    #     for s in strs:
    #         dic[tuple(sorted(s))].append(s)
    #     return list(dic.values())

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for word in strs:
            dic[tuple(sorted(word))].append(word)
        # print(isinstance(iter(dic.values()), collections.Iterator))  # 加了 iter 就变成了迭代器，哈哈，不加是可迭代对象
        return list(dic.values())


s = Solution()
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(a))
