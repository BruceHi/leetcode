# 1013. 将数组分成和相等的三部分
from typing import List


class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        arr_sum = sum(arr)
        if arr_sum % 3:
            return False
        target = arr_sum // 3
        count = 0
        res = []
        for i, num in enumerate(arr):
            count += num
            if count == target:
                res.append(i)
                count = 0
        return len(res) == 3 or (len(res) > 3 and not target)


s = Solution()
arr = [0,2,1,-6,6,-7,9,1,2,0,1]
print(s.canThreePartsEqualSum(arr))

arr = [0,2,1,-6,6,7,9,-1,2,0,1]
print(s.canThreePartsEqualSum(arr))

arr = [3,3,6,5,-2,2,5,1,-9,4]
print(s.canThreePartsEqualSum(arr))

arr = [10,-10,10,-10,10,-10,10,-10]
print(s.canThreePartsEqualSum(arr))
