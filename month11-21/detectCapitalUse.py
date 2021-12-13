# 520. 检测大写字母
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # return word in (word.upper(), word.capitalize(), word.lower())
        return word.isupper() or word.islower() or word.istitle()

s = Solution()
word = "USA"
print(s.detectCapitalUse(word))

word = "FlaG"
print(s.detectCapitalUse(word))
