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

    # def patternMatching(self, pattern: str, value: str) -> bool:
    #     if len(pattern) == 1:
    #         return True
    #     if not len(value) and len(pattern) > 1:
    #         return False
    #     # reg_a = '\\1' if pattern[0] == 'a' else '\\2'
    #     # reg_b = '\\1' if pattern[0] == 'b' else '\\2'
    #     reg_a, reg_b = ('\\1', '\\2') if pattern[0] == 'a' else ('\\2', '\\1')
    #     p = '^' + pattern.replace('a', '(\\w*)', 1).replace('b', '(\\w*)', 1) \
    #         .replace('a', reg_a).replace('b', reg_b) + '$'  # 使用 \\，防止转义
    #     p = re.compile(p)
    #     if p.match(value):
    #         return True
    #     return False

    # 最后一条未通过
    # def patternMatching(self, pattern: str, value: str) -> bool:
    #     if len(pattern) == 1:
    #         return True
    #     if not len(value) and len(pattern) > 1:
    #         return False
    #     reg_a, reg_b = (r'\1', r'\2') if pattern[0] == 'a' else (r'\2', r'\1')
    #     # 正则表达式 * 号不能去掉，首尾标志符不能忘，在字符串前面加 r 变为原始字符串
    #     p = '^' + pattern.replace('a', r'(\w*)', 1).replace('b', r'(\w*)', 1)\
    #         .replace('a', reg_a).replace('b', reg_b) + '$'
    #     print(p)
    #     p = re.compile(p)
    #     if p.match(value):
    #         return True
    #     return False

    def patternMatching(self, pattern: str, value: str) -> bool:
        if len(pattern) == 1:
            return True
        if not value and len(pattern) > 1:
            return False
        reg_a, reg_b = (r'\1', r'\2') if pattern[0] == 'a' else (r'\2', r'\1')
        p = '^' + pattern.replace('a', r'(\w*)', 1).replace('b', r'(\w*)', 1).\
            replace('a', reg_a).replace('b', reg_b) + '$'
        p = re.compile(p)
        res = p.match(value)

        if res:
            groups = res.groups()
            if len(groups) == 1 or groups[0] != groups[1]:   # len(groups) == 1的情况比如 ‘aaaa’
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
print(s.patternMatching(pattern, value))  # "a"="dogdog",b=""，

pattern = "a"
value = ""
print(s.patternMatching(pattern, value))  # 应该为 True

pattern = "ab"
value = ""
print(s.patternMatching(pattern, value))  # 应该为 False "a"和"b"不能同时表示相同的字符串。

pattern = "bbbaa"
value = "xxxxxxy"
print(s.patternMatching(pattern, value))  # 应该为 False

pattern = "abbaa"
value = "dogdogdogdogdog"
print(s.patternMatching(pattern, value))  # False a 与 b 不能表示相同的字符串

pattern = "ab"
value = "big123"
print(s.patternMatching(pattern, value))

pattern = "bbb"
value = "xxxxxx"
print(s.patternMatching(pattern, value))
