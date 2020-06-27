# 字母异位词分组
from typing import List
from collections import defaultdict


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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)
        return list(dic.values())


s = Solution()
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(a))
