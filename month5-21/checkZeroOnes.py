class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        def long_seq(s, t):
            i = 0
            res = 0
            for j, c in enumerate(s):
                if c != t:
                    res = max(res, j-i)
                    i = j + 1
            if s[-1] == t:
                res = max(res, len(s)-i)
            return res
        return long_seq(s, '1') > long_seq(s, '0')



obj = Solution()
s = "1101"
print(obj.checkZeroOnes(s))

s = "111000"
print(obj.checkZeroOnes(s))

s = "110100010"
print(obj.checkZeroOnes(s))

s = "1"
print(obj.checkZeroOnes(s))
