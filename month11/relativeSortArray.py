# 数组的相对排序
from collections import Counter
from typing import List


class Solution:
    # def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    #     count = Counter(arr1)
    #     res = []
    #     for num in arr2:
    #         res.extend([num] * count[num])
    #     arr2 = set(arr2)
    #     remain = sorted(filter(lambda x: x not in arr2, arr1))
    #     res.extend(remain)
    #     return res

    # 自定义排序，排序规则一：在 arr2 里面的先排序，二：按照对应索引进行排序
    # def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    #     rank = {x: i for i, x in enumerate(arr2)}
    #
    #     def mycmp(x):
    #         return (0, rank[x]) if x in rank else (1, x)
    #
    #     arr1.sort(key=mycmp)
    #     return arr1

    # # 自定义排序，将在 arr2 里面的数值转为负数索引，自然排序就排在前面了。
    # def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
    #     n = len(arr2)
    #     rank = {x: i-n for i, x in enumerate(arr2)}
    #
    #     def mycmp(x):
    #         return rank[x] if x in rank else x
    #
    #     arr1.sort(key=mycmp)
    #     return arr1

    # 计数排序
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        m = max(arr1)
        count = [0] * (m+1)

        for num in arr1:
            count[num] += 1

        res = []
        for num in arr2:
            res.extend([num] * count[num])
            count[num] = 0

        for i in range(m+1):
            if count[i]:
                res.extend([i] * count[i])
        return res




s = Solution()
arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
print(s.relativeSortArray(arr1, arr2))

arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]
print(s.relativeSortArray(arr1, arr2))

