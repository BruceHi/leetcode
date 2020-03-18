# class Solution:
#     def countAndSay(self, n: int) -> str:
#         if n == 1:
#             return '1'
#         s = self.countAndSay(n-1)
#
#         count, num, i = 0, 0, 0
#         while i < len(s):
#             j = i
#             while j < len(s) and s[i] == s[j]:  # 不能放反了,否则溢出时会报错
#                 count += 1
#                 j += 1
#             num = num*100 + count*10 + int(s[i])
#             i += count
#             count = 0
#
#         return str(num)


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n-1)

        count, i, res = 0, 0, ''  # res代表result.
        while i < len(s):
            j = i
            while j < len(s) and s[i] == s[j]:
                count += 1
                j += 1
            res += str(count) + s[i]
            i += count
            count = 0

        return res


s = Solution()
n = 1
print(s.countAndSay(n))

n = 2
print(s.countAndSay(n))

n = 3
print(s.countAndSay(n))

n = 4
print(s.countAndSay(n))

n = 5
print(s.countAndSay(n))