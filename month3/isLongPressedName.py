# 925.长按键入
import re


class Solution:
    # # 正则表达式
    # def isLongPressedName(self, name: str, typed: str) -> bool:
    #     if len(name) > len(typed):
    #         return False
    #     if len(name) == len(typed):
    #         return name == typed
    #     pattern = '^'+'+'.join(name) + '+'+'$'
    #     pattern = re.compile(pattern)
    #     return bool(pattern.match(typed))

    # 双指针
    def isLongPressedName(self, name: str, typed: str) -> bool:
        m, n = len(name), len(typed)
        i, j = 0, 0
        while j < n:
            if i < m and name[i] == typed[j]:
                i, j = i+1, j+1
            elif j > 0 and typed[j] == typed[j-1]:
                j += 1
            else:
                return False
        return i == m



s = Solution()
name = "alex"
typed = "aaleex"
print(s.isLongPressedName(name, typed))

name = "saeed"
typed = "ssaaedd"
print(s.isLongPressedName(name, typed))

name = "leelee"
typed = "lleeelee"
print(s.isLongPressedName(name, typed))

name = "laiden"
typed = "laiden"
print(s.isLongPressedName(name, typed))

name = "alex"
typed = "aaleexa"
print(s.isLongPressedName(name, typed))
