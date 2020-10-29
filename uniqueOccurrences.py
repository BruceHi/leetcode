from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        return len(dic) == len(set(dic.values()))


s = Solution()
arr = [1,2,2,1,1,3]
print(s.uniqueOccurrences(arr))

arr = [1,2]
print(s.uniqueOccurrences(arr))

arr = [-3,0,1,-3,1,1,1,-3,10,0]
print(s.uniqueOccurrences(arr))

arr = []
print(s.uniqueOccurrences(arr))
