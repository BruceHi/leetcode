from collections import Counter


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        counts = []
        for c in text.split():
            counts.append(Counter(c))
        res = 0
        for count in counts:
            flag = 1
            for c in brokenLetters:
                if c in count:
                    flag = 0
                    continue
            if flag:
                res += 1
        return res



s = Solution()
text = "hello world"
brokenLetters = "ad"
print(s.canBeTypedWords(text, brokenLetters))

text = "leet code"
brokenLetters = "lt"
print(s.canBeTypedWords(text, brokenLetters))

text = "leet code"
brokenLetters = "e"
print(s.canBeTypedWords(text, brokenLetters))