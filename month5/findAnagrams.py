# 找到字符串中所有字母异位词(滑动窗口)
from typing import List
from collections import OrderedDict
from collections import Counter
from collections import defaultdict


class Solution:

    # 若 p 中所有单词都不同，OK
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     res, record = [], OrderedDict()
    #     for i, c in enumerate(s):
    #         if c not in p:
    #             record.clear()
    #         else:
    #             record[c] = i
    #             if len(record) == len(p):
    #                 _, val = record.popitem(last=False)
    #                 res.append(val)
    #     return res

    # # 超时
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     res, left = [], 0
    #     for i, c in enumerate(s):
    #         if c not in p:
    #             left = i + 1
    #
    #         elif i - left + 1 == len(p):
    #             if sorted(s[left:i+1]) == sorted(p):
    #                 res.append(left)
    #             left += 1
    #
    #     return res

    # # i 就相当于 right
    # # Counter 类型是 dict 的字类，所以可以直接相等判断。也可以使用 dict() 进行判断。
    # def findAnagrams(self, s: str, p: str) -> List[int]:
    #     count = Counter(p)
    #     res, left = [], 0
    #     dic = {}
    #     for i, c in enumerate(s):
    #         if c not in count:
    #             left = i + 1
    #             dic.clear()
    #         else:
    #             dic[c] = dic.get(c, 0) + 1
    #             if i - left + 1 == len(p):
    #                 if dic == count:
    #                     res.append(left)
    #
    #                 dic[s[left]] -= 1
    #                 if dic[s[left]] == 0:
    #                     dic.pop(s[left])
    #                 left += 1
    #     return res

    def findAnagrams(self, s: str, p: str) -> List[int]:
        count = Counter(p)
        res, left = [], 0
        dic = defaultdict(int)

        for i, c in enumerate(s):
            if c not in count:
                left = i + 1
                dic.clear()
            else:
                dic[c] += 1
                if i - left + 1 == len(p):
                    if dic == count:
                        res.append(left)
                    dic[s[left]] -= 1
                    if dic[s[left]] == 0:
                        dic.pop(s[left])
                    left += 1
        return res


obj = Solution()
s = "cbaebabacd"
p = "abc"
print(obj.findAnagrams(s, p))

s = "abab"
p = "ab"
print(obj.findAnagrams(s, p))

s = "baa"
p = "aa"
print(obj.findAnagrams(s, p))
