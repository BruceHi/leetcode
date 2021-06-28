from collections import Counter


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        def iswonderful(word):
            count = Counter(word)
            ans = 0
            for v in count.values():
                if v & 1:
                    ans += 1
            return ans <= 1

        n = len(word)
        res = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if iswonderful(word[i:j]):
                    res += 1
        return res


s = Solution()
word = "aba"
print(s.wonderfulSubstrings(word))

word = "aabb"
print(s.wonderfulSubstrings(word))

word = "he"
print(s.wonderfulSubstrings(word))

