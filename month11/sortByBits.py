# 根据数字二进制下的 1 的数目排序
from typing import List


class Solution:
    # def sortByBits(self, arr: List[int]) -> List[int]:
    #     dic = {}
    #     for i, num in enumerate(arr):
    #         if num not in dic:
    #             count = 1
    #             while num:
    #                 count += 1
    #                 num &= num - 1
    #             dic[arr[i]] = count
    #
    #     arr.sort(key=lambda x: (dic[x], x))  # 按第一顺序排序，若第一顺序相同，按第二顺序排序。
    #     return arr

    def sortByBits(self, arr: List[int]) -> List[int]:
        dic = {}
        for num in arr:
            dic[num] = bin(num).count('1')
        arr.sort(key=lambda x: (dic[x], x))  # 按第一顺序排序，若第一顺序相同，按第二顺序排序。
        return arr

s = Solution()
arr = [0,1,2,3,4,5,6,7,8]
print(s.sortByBits(arr))

arr = [1024,512,256,128,64,32,16,8,4,2,1]
print(s.sortByBits(arr))

arr = [10000,10000]
print(s.sortByBits(arr))

arr = [2,3,5,7,11,13,17,19]
print(s.sortByBits(arr))

arr = [10,100,1000,10000]
print(s.sortByBits(arr))
