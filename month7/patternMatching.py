# 模式匹配
# 1 <= len(pattern) <= 1000
# 0 <= len(value) <= 1000
import re


class Solution:

    # 失败
    # def patternMatching(self, pattern: str, value: str) -> bool:
    #     m, n = len(pattern), len(value)
    #     if not n and m > 1:
    #         return False
    #     if not n and m == 1:
    #         return True
    #     pos = n // m
    #     if pos != n / m:
    #         return False
    #     record = {}
    #     for i, p in enumerate(pattern):
    #         tmp = value[pos*i:pos*(i+1)]
    #         if p not in record:
    #             record[p] = tmp
    #         elif record[p] != tmp:
    #             return False
    #     return True

    def patternMatching(self, pattern: str, value: str) -> bool:
        if len(pattern) == 1:
            return True
        if not len(value) and len(pattern) > 1:
            return False
        # reg_a = '\\1' if pattern[0] == 'a' else '\\2'
        # reg_b = '\\1' if pattern[0] == 'b' else '\\2'
        reg_a, reg_b = ('\\1', '\\2') if pattern[0] == 'a' else ('\\2', '\\1')
        p = '^' + pattern.replace('a', '(\\w*)', 1).replace('b', '(\\w*)', 1) \
            .replace('a', reg_a).replace('b', reg_b) + '$'  # 使用 \\，防止转义
        p = re.compile(p)
        if p.match(value):
            return True
        return False


s = Solution()
pattern = "abba"
value = "dogcatcatdog"
print(s.patternMatching(pattern, value))

pattern = "abba"
value = "dogcatcatfish"
print(s.patternMatching(pattern, value))

pattern = "aaaa"
value = "dogcatcatdog"
print(s.patternMatching(pattern, value))

pattern = "abba"
value = "dogdogdogdog"
print(s.patternMatching(pattern, value))

pattern = "a"
value = ""
print(s.patternMatching(pattern, value)) # 应该为 True

pattern = "ab"
value = ""
print(s.patternMatching(pattern, value))  # 应该为 False

pattern = "bbbaa"
value = "xxxxxxy"
print(s.patternMatching(pattern, value))  # 应该为 False
