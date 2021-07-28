class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res = ''
        for c in s:
            res += str(ord(c) - ord('a') + 1)

        ans = 0
        for _ in range(k):
            ans = 0
            for c in res:
                ans += int(c)
            res = str(ans)
        return ans


obj = Solution()
s = "iiii"
k = 1
print(obj.getLucky(s, k))

s = "leetcode"
k = 2
print(obj.getLucky(s, k))
