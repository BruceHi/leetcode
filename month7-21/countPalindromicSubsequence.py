class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = 0
        record = set()
        n = len(s)
        for i in range(n-2):
            for j in range(n-1, i+1, -1):
                if s[i] in record:
                    break
                if s[i] == s[j]:
                    res += len(set(s[i+1:j]))
                    break
            record.add(s[i])
        return res


obj = Solution()
s = "aabca"
print(obj.countPalindromicSubsequence(s))

s = "abc"
print(obj.countPalindromicSubsequence(s))

s = "bbcbaba"
print(obj.countPalindromicSubsequence(s))
