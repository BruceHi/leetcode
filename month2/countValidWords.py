# 2047. 句子中的有效单词数
import re


class Solution:
    def countValidWords(self, sentence: str) -> int:
        p = r'^([a-z]+(-[a-z]+)?)?[!.,]?$'
        p = re.compile(p)
        res = 0
        for sen in sentence.split():
            if p.match(sen):
                res += 1
        return res


# ! 也算一个单词
s = Solution()
sentence = "cat and  dog"
print(s.countValidWords(sentence))

sentence = "!this  1-s b8d!"
print(s.countValidWords(sentence))

sentence = "alice and  bob are playing stone-game10"
print(s.countValidWords(sentence))

sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
print(s.countValidWords(sentence))

sentence = "!"
print(s.countValidWords(sentence))
