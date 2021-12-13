# 859. 亲密字符串
from collections import Counter


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        count1, count2 = Counter(s), Counter(goal)
        if count1 != count2:
            return False
        if s == goal:
            return max(count1.values()) > 1
        res = 0
        for a, b in zip(s, goal):
            if a != b:
                res += 1
        return res == 2


obj = Solution()
s = "ab"
goal = "ba"
print(obj.buddyStrings(s, goal))

s = "ab"
goal = "ab"
print(obj.buddyStrings(s, goal))

s = "aa"
goal = "aa"
print(obj.buddyStrings(s, goal))

s = "aaaaaaabc"
goal = "aaaaaaacb"
print(obj.buddyStrings(s, goal))
