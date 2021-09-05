from itertools import combinations



class Solution:
    # def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
    #     def func1(x: str):
    #         if len(x) == 1:
    #             return True
    #         return not x.startswith('0')
    #
    #     res = []
    #     for i in range(len(binary)):
    #         res.extend(filter(func1, [''.join(x) for x in combinations(binary, i+1)]))
    #     return len(set(res))

    # 超时
    # def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
    #     def func1(x: tuple):
    #         if len(x) == 1:
    #             return True
    #         return x[0] != '0'
    #
    #     res = []
    #     for i in range(len(binary)):
    #         res.extend(list(filter(func1, combinations(binary, i + 1))))
    #     return len(set(res))


    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:

        pass


s = Solution()
binary = "001"
print(s.numberOfUniqueGoodSubsequences(binary))

binary = "11"
print(s.numberOfUniqueGoodSubsequences(binary))

binary = "101"
print(s.numberOfUniqueGoodSubsequences(binary))

# 超时
binary = "111001101100000001001110110101110001100"
print(s.numberOfUniqueGoodSubsequences(binary))

