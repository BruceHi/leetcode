class Solution:
    # def cftHireFunc(self, arr):
    #     arr.sort()
    #     n = len(arr)
    #     i = 1
    #     for num in arr:
    #         if num > 0:
    #             if i != num:
    #                 return i
    #             i += 1
    #     return n


    # def cftHireFunc(self, arr):
    #     arr = list(filter(lambda x: x > 0, arr))
    #     if not arr:
    #         return 1
    #     arr.sort()
    #
    #
    #     i = 1
    #     for num in arr:
    #         if i != num:
    #             return i
    #         i += 1
    #     return arr[-1]+1


    # def cftHireFunc(self, arr):
    #     if not arr:
    #         return 1
    #     arr.sort()
    #
    #     i = 1
    #     for num in arr:
    #         if num > 0:
    #             if i != num:
    #                 return i
    #             i += 1
    #     return arr[-1]+1

    def cftHireFunc(self, arr):
        arr = set(arr)
        n = len(arr)
        for i in range(1, n+2):
            if i not in arr:
                return i

s = Solution()
arr = [8, -1, 3, 9, 5]
print(s.cftHireFunc(arr))

arr = [0, 1, 2, 3, 4, 5, 6, 7]
print(s.cftHireFunc(arr))

arr = [1, 2]
print(s.cftHireFunc(arr))

arr = []
print(s.cftHireFunc(arr))

arr = [2]
print(s.cftHireFunc(arr))

arr = [3]
print(s.cftHireFunc(arr))
