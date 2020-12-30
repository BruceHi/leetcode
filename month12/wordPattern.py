# 290.单词规律
class Solution:
    # def wordPattern(self, pattern: str, s: str) -> bool:
    #     arr = s.split(' ')
    #     if len(pattern) != len(arr):
    #         return False
    #     record = {}
    #     for i, c in enumerate(pattern):
    #         if c in record:
    #             if record[c] != arr[i]:
    #                 return False
    #         else:
    #             if arr[i] in record.values():
    #                 return False
    #             record[c] = arr[i]
    #     return True

    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        if len(pattern) != len(arr):
            return False
        record = {}
        for p, c in zip(pattern, arr):
            if p in record:
                if record[p] != c:
                    return False
            else:
                if c in record.values():
                    return False
                record[p] = c
        return True


obj = Solution()
pattern = "abba"
s = "dog cat cat dog"
print(obj.wordPattern(pattern, s))

pattern = "abba"
s = "dog cat cat fish"
print(obj.wordPattern(pattern, s))

pattern = "aaaa"
s = "dog cat cat dog"
print(obj.wordPattern(pattern, s))

pattern = "abba"
s = "dog dog dog dog"
print(obj.wordPattern(pattern, s))

pattern = "aaa"
s = "aa aa aa aa"
print(obj.wordPattern(pattern, s))
