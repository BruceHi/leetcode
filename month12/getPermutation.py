# 60. 排序序列
from itertools import permutations


class Solution:
    # def getPermutation(self, n: int, k: int) -> str:
    #     res = list(permutations(range(1, n+1)))[k-1]
    #     return ''.join(map(str, res))

    def getPermutation(self, n: int, k: int) -> str:
        nums = permutations(range(1, n+1))
        print(list(nums))
        # for _ in range(k-1):
        #     next(nums)
        # res = next(nums)
        # return ''.join(map(str, res))


s = Solution()
n = 3
k = 3
print(s.getPermutation(n, k))

n = 4
k = 9
print(s.getPermutation(n, k))

n = 3
k = 1
print(s.getPermutation(n, k))
