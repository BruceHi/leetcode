# 567.字符串的排列
from itertools import permutations
from collections import Counter

class Solution:
    # 超时
    # def checkInclusion(self, s1: str, s2: str) -> bool:
    #     for str_tuple in permutations(s1):
    #         if ''.join(str_tuple) in s2:
    #             return True
    #     return False

    # 使用滑动窗口
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        left, right = 0, m-1
        counter1 = Counter(s1)
        counter2 = Counter(s2[:right])

        while right < n:
            counter2[s2[right]] += 1
            if counter1 == counter2:
                return True
            left_val = s2[left]
            counter2[left_val] -= 1
            if counter2[left_val] == 0:
                counter2.pop(left_val)
            left, right = left+1, right+1
            # right 必须要放在最后
        return False






s = Solution()
s1 = "ab"
s2 = "eidbaooo"
print(s.checkInclusion(s1, s2))

s1 = "ab"
s2 = "eidboaoo"
print(s.checkInclusion(s1, s2))

s1 = "ba"
s2 = "eidboaoo"
print(s.checkInclusion(s1, s2))