# 宝石与石头
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count, diamond = 0, set(J)
        for c in S:
            if c in diamond:
                count += 1
        return count


s = Solution()
J = "aA"
S = "aAAbbbb"
print(s.numJewelsInStones(J, S))

J = "z"
S = "ZZ"
print(s.numJewelsInStones(J, S))